#!/usr/bin/pup
# Using Puppet, install flask from pip3
package { 'python3-pip':
  ensure => 'present',
}

package { 'flask':
  ensure   => 'installed',
  provider => 'pip',
  require  => Package['python3-pip'],
}

package { 'werkzeug':
  ensure   => 'installed',
  provider => 'pip',
  require  => Package['python3-pip'],
}
