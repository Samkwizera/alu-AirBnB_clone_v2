# Puppet manifest to set up web static deployment

package { 'nginx':
  ensure => 'present',
}

file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static/releases':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static/shared':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => "server {\n    listen 80 default_server;\n    listen [::]:80 default_server;\n    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }\n    location / {\n        try_files \$uri \$uri/ =404;\n    }\n}",
  owner   => 'root',
  group   => 'root',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
} 