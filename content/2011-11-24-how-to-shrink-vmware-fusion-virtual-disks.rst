How to shrink VMware Fusion virtual disks
#########################################
:date: 2011-11-24 09:32
:category: Server
:tags: virtual disk, vmware
:slug: how-to-shrink-vmware-fusion-virtual-disks

VMWare has an included tool (vmware-vdiskmanager) for shrinking virtual
disks. But before performing the shrink you need to zero out the unused
disk space first. So start your VM and do a

``dd if=/dev/zero of=/empty_file; rm /empty_file`` 

After that, shut down the VM and start the vmware-vdiskmanager, which is located in
/Applications/VMware Fusion.app/Contents/Library (OSX 10.7.2, VMware
Fusion 4) and shrink the disk:

``./vmware-vdiskmanager -k pathtodisk.vmdk``
