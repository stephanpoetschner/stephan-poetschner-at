# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
   config.vm.box = "bento/ubuntu-16.04"

   config.vm.provision :shell, path: "vagrant-setup/provision.sh", privileged: false

   config.ssh.forward_agent = true

   # For better performance on unix-systems use NFS (needs host-support).
   # For easier setup disable these lines and enable the line above.
   config.vm.network "private_network", ip: '192.168.71.59'
   config.vm.hostname = "dev.stephan-poetschner.at"

   config.vm.synced_folder '.', '/vagrant'
end

