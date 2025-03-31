# virt-gmod

**virt-gmod** é um front-end simples e eficiente para o **[virt-qmod](https://github.com/elppans/virt-qmod)**, um script poderoso para gerenciar Máquinas Virtuais (VMs) utilizando QEMU/KVM. O objetivo principal do virt-gmod é fornecer uma interface gráfica acessível e direta ao ponto para facilitar o gerenciamento básico de VMs com apenas alguns cliques.

## Funcionalidades
O virt-gmod oferece as seguintes funcionalidades básicas:
- **Criar Máquina Virtual**: Crie VMs usando uma configuração pré-definida, ou personalize parâmetros como Nome, RAM, vCPUs, Disco, CD-ROM, Rede e Gráficos de forma opcional.
- **Listar Máquinas Virtuais**: Visualize as VMs disponíveis no sistema.
- **Iniciar/Parar uma VM**: Controle facilmente o estado das VMs.
- **Remover uma VM**: Exclua VMs desnecessárias.
- **Abrir VMs em modo gráfico**: Acesse as VMs em execução com uma interface gráfica (Virt Viewer).
- **Gerenciamento de Snapshots**: Liste, crie e exclua snapshots de uma VM.
- **Gerenciamento de Discos**: Visualize informações, redimensione e encolha discos, bem como anexe/desanexe ISOs.

## Como Usar
Ao iniciar o **virt-gmod**, você verá uma interface gráfica com as opções abaixo:
1. Criar Máquina Virtual
2. Listar VMs
3. Iniciar VM
4. Parar VM
5. Remover VM
6. Abrir VM em Virt Viewer
7. Editar Configurações da VM
8. Listar Snapshots
9. Criar Snapshot
10. Deletar Snapshot
11. Mostrar Informações do Disco
12. Redimensionar Disco
13. Encolher Disco
14. Anexar ISO
15. Desanexar ISO
16. Sair

Ao clicar em uma opção, o script executará a ação correspondente utilizando os comandos do **virt-qmod**.

## Exemplo de Uso do virt-qmod
Se preferir usar o virt-qmod diretamente, abaixo estão exemplos de comandos:
```bash
# Criar uma VM com configuração padrão
virt-qmod create --name minhaVM --cdrom /caminho/para/iso.iso

# Criar uma VM personalizada
virt-qmod create --name minhaVM --ram 2048 --vcpus 2 --disk 20G --cdrom /caminho/para/iso.iso --network default --graphics spice --os-variant ubuntu20.04

# Listar VMs
virt-qmod list

# Iniciar uma VM
virt-qmod start minhaVM

# Parar uma VM
virt-qmod stop minhaVM

# Remover uma VM
virt-qmod remove minhaVM
```

## Atualizações Recentes
- **04/03/2025**: Adicionada a funcionalidade "Action Menu" no Dolphin para criar e iniciar VMs diretamente com o botão direito do mouse sobre a ISO.

## Autor
Desenvolvido por **Marcelo (Elppans)**  
Contato: `<marcelo*@email*>`

## Licença
Este projeto está licenciado sob a **Licença MIT**. Para mais detalhes, consulte o arquivo LICENSE.

---
