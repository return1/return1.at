Ubuntu EC2 AMI with XFS root EBS Volume (10.04 LTS, Lucid Lynx)
###############################################################
:date: 2011-10-25 22:33
:category: Server
:tags: amazon web services, ami, aws, ebs, ec2, grub, lucid lynx, ubuntu, xfs
:slug: ubuntu-ec2-ami-with-xfs-root-ebs-volume-10-04-lts-lucid-lynx

Are you also in need of a current Ubuntu LTS (10.04, Lucid Lynx) AMI for
Amazon Web Services, with EBS Boot and XFS as file system? Maybe because
you would like to make consistent snapshots via xfs\_freeze and
`ec2\_consistent\_snapshot`_? Then this `article`_ by Scott Moser helps
you out. But hey. It will not work, because latest 10.04 Ubuntu EC2 AMIs
have their boot partition labeled
``cloudimg-rootfs``, which is too long for an XFS
file system label, XFS supports only 12 characters. Ubuntu´s Maverick
and Natty AMIs for EC2 have already been fixed, the label there is
``uec-rootfs``. If you follow Scott´s instructions
from the link above, your system will not boot, the error looks like
this: 

	ALERT! /dev/disk/by-label/cloudimg-rootfs does not exist. Dropping to a shell!

All you have to do is change the label of the XFS partition from ``cloudimg-rootfs`` to 
``uec-rootfs``, also replace the old label in

-  /boot/grub/menu.lst
-  /boot/grub/grub.cfg
-  /etc/fstab (missed that, thanks @scott)

I have built an AMI, complete with above steps. So you can launch Ubuntu
10.04 LTS Lucid Lynx, with EBS root and XFS: https://console.aws.amazon.com/ec2/home?region=eu-west-1#launchAmi=ami-61c4f615


.. _ec2\_consistent\_snapshot: http://alestic.com/2009/09/ec2-consistent-snapshot
.. _article: http://ubuntu-smoser.blogspot.com/2010/11/create-image-with-xfs-root-filesystem.html
