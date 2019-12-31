# i3-jinja-config

[jinja]: https://jinja.palletsprojects.com/templates/

Create an i3 config from Jinja2 template.

## Why?

I am managing multiple computers and my configuration depends on 
screen/display keyboard etc... ... depend on *hostname*.

[Jinja2 temlate][jinja]
allows me to use **conditions** and to **include** configs into config.

## Inspiration

* https://github.com/kenyonj/i3-create-config


## Usege

Save the `jinja-create-config.py` in your `~/.i3` directory and save your
configuration into `~/.i3/config.j2` instead `~/.i3/config`.


... in your `~/.xinitrc` or `~/.Xsession`


```sh
#create i3 config
~/.i3/jinja-create-config.py

#start i3
exec i3
```


... in your i3 configuration `~/.i3/config.j2`


```jinja
{%- if hostname == 'foo' %}
  set $primary DVI-I-1
  set $secondary VGA-1

  set $STATUS_FONT pango:Terminus 15
  set $STATUS_CONFFILE ~/.i3/i3blocks_foo.conf
{%- else %}
  set $primary DVI-1
  set $secondary VGA-0

  set $STATUS_FONT pango:Terminus 22
  set $STATUS_CONFFILE ~/.i3/i3blocks_bar.conf
{%- endif %}

# ...

bar {
    status_command i3blocks -c $STATUS_CONFFILE
    font $STATUS_FONT
    output $primary
    position top
    tray_output primary
}

```

... call `jinja-create-config.py` by reload and restart. 

```sh
# Yes really is necessary use i3-msg
# reload the configuration file
bindsym $mod+Shift+c exec "~/.i3/jinja-create-config.py; i3-msg reload"
# restart i3 inplace (preserves your layout/session, can be used to upgrade i3)
bindsym $mod+Shift+r exec "~/.i3/jinja-create-config.py; i3-msg restart"
```

If you want split the configuration into multiple files:

```jinja
# Floating windows
{% include 'floating.j2' %}
```

Use the force of [Jinja  templating language][jinja].
