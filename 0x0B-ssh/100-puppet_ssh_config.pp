# Puppet manifest to create ssh config file

include stdlib

file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '	 PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => '	 IdentityFile ~/.ssh/school',
}
