import os
import pathlib
from gi.repository import Nautilus, GObject

class VirtGmodExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()

    def launch_command(self, menu, files, mode):
        # Pega o caminho completo do arquivo
        file_path = files[0].get_location().get_path()
        # Pega apenas o nome do arquivo sem a extensão .iso (basename)
        vm_name = pathlib.Path(file_path).stem
        
        # Define os comandos baseados no modo selecionado
        if mode == "uefi":
            cmd = f"virt-qmod create --name '{vm_name}' --cdrom '{file_path}' && virt-qmod start '{vm_name}' && virt-qmod open '{vm_name}'"
        
        elif mode == "legacy":
            cmd = f"virt-qmod create --name '{vm_name}' --cdrom '{file_path}' --boot hd && virt-qmod start '{vm_name}' && virt-qmod open '{vm_name}'"
        
        elif mode == "remove":
            # Executa a remoção e, se tiver sucesso (&&), mostra os avisos do Zenity
            cmd = (
                f"virt-qmod stop_force '{vm_name}' ; "
                f"virt-qmod remove '{vm_name}' && "
                f"zenity --notification --text='Removido a VM {vm_name}!' && "
                f"zenity --info --text='Removido a VM {vm_name}!'"
            )

        # Executa o comando em background para não travar o Nautilus
        os.system(f"{cmd} &")

    def get_file_items(self, *args):
        files = args[-1] if len(args) > 1 else (args[0] if args else [])
        
        if not files or len(files) != 1:
            return []

        file = files[0]
        if not file.get_uri().lower().endswith('.iso'):
            return []

        # 1. Criar e Iniciar VM (UEFI/Padrão)
        item_uefi = Nautilus.MenuItem(
            name="VirtGmod::CreateUEFI",
            label="Criar E Iniciar VM",
            tip="Criar VM UEFI usando esta ISO"
        )
        item_uefi.connect("activate", self.launch_command, [file], "uefi")

        # 2. Criar e Iniciar VM (Legacy)
        item_legacy = Nautilus.MenuItem(
            name="VirtGmod::CreateLegacy",
            label="Criar E Iniciar VM (Legacy)",
            tip="Criar VM BIOS/Legacy usando esta ISO"
        )
        item_legacy.connect("activate", self.launch_command, [file], "legacy")

        # 3. Remover VM
        item_remove = Nautilus.MenuItem(
            name="VirtGmod::Remove",
            label="Remover VM",
            tip="Remover a VM associada a esta ISO"
        )
        item_remove.connect("activate", self.launch_command, [file], "remove")

        return [item_uefi, item_legacy, item_remove]
