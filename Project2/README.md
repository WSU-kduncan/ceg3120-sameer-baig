# Project 2

## Part 1 - Build A VPC

1) VPC: A VPC is just a personal network hosted on the cloud that is connected to one's AWS account.
2) Subnet: Range of IP addresses that will be conncetd to the VPC. It determines how many devices can be connected to the VPC.
3) Internet Gateway: Connects the VPC to the internet.
4) Route Table: Determines which IP addresses the network traffic will be directed to. 
5) Security Group: Set of rules that controls whatever network traffic is going in or out.

## Part 2 - EC2 Instances

1) -AMI Selected: Ubuntu Server 22.04 LTS (HVM)
	- Default Username: Ubuntu
	- AMI ID: ami-08c40ec9ead489470
   -Instance Type: t2.micro
2) Under Network Settings when creating the instance, change the VPC from the default to the one you created. Differentiate the VPC with the tags created for the VPC.
3) A public IPv4 address will not be automatically assigned, and I will instead opt for a elastic IP address as I want the IP address to remain static for the duration of the instance. 
4) While creating the instance, go under the Configure Storage tab, and there you can configure how much storage and what type you want for the instance. 
5) When making the instance, it will automacially prompt you for the name of the instance, which already has the Name Key already designated.
6) Under Network Settings, after associating the VPC, choose `Select Existing Security Group` and then choose the security group with the tag you assigned. 
7) Under Network & Security, click on `Elastic IP` and then choose `Allocate an Elastic IP`. After adding the appropiate tag and allocating the IP address, click on the new IP and then click on Associate Elastic IP Address. Here the instance you created will pop up, and a Private IP address will also be allocated.   
8) Image in Images folder.
9) After logging on to the instance, the command `sudo hostnamectl set-hostname Baig-Ubuntu` will change the hostname after rebooting the instance. 
10) Image in Images folder.
