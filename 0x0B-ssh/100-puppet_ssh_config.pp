#!/usr/bin/env bash
# puppet manifest to make changes on config file

file { 'config':
  ensure  => present,
  owner   => 'root',
  path    => '/etc/ssh/ssh_config',
  content => 'IdentityFile ~/.ssh/school\n PasswordAuthentication no\n User ubuntu\n Host 100.26.9.92\n',
}
