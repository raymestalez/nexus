/*
Errno::ENOENT: No such file or directory @ rb_sysopen - style.scss

Backtrace:
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/plugin/compiler.rb:482:in `read'
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/plugin/compiler.rb:482:in `update_stylesheet'
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/plugin/compiler.rb:215:in `block in update_stylesheets'
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/plugin/compiler.rb:209:in `each'
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/plugin/compiler.rb:209:in `update_stylesheets'
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/plugin/compiler.rb:293:in `watch'
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/plugin.rb:108:in `method_missing'
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/exec/sass_scss.rb:381:in `watch_or_update'
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/exec/sass_scss.rb:51:in `process_result'
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/exec/base.rb:52:in `parse'
/var/lib/gems/2.1.0/gems/sass-3.4.14/lib/sass/exec/base.rb:19:in `parse!'
/var/lib/gems/2.1.0/gems/sass-3.4.14/bin/sass:13:in `<top (required)>'
/usr/local/bin/sass:23:in `load'
/usr/local/bin/sass:23:in `<main>'
*/
body:before {
  white-space: pre;
  font-family: monospace;
  content: "Errno::ENOENT: No such file or directory @ rb_sysopen - style.scss"; }
