Dropbox
=======

A "dropbox" is a directory that gives isolated bits to a particular
person. Think of it as a Public that is specific to just one person
and that that person also has write access to. You can put a file in
there for them to view or vice-versa. Conveniently, it is also
cert-protected so that only they can view it online.

There is no relationship to Dropbox(TM), the file synchronization and
storage system. For that, see http://www.dropbox.com.

Setup
-----

To set up, you first need to create a "dropbox list" --- a moira list
which will be used to keep track of who you have set up dropboxes
for. By default, the name of this list is $USER-dropbox
(e.g. leonidg-dropbox); if you choose something else, you should set
the environment variable $DROPBOXLIST.

The dropboxes will all be stored in a central "dropbox repository,"
which is a directory you should have write access to. By default, this
is $HOME/dropbox (e.g. /mit/leonidg/dropbox); if you choose something
else, you should set the environemnt variable $DROPBOXDIR.  **THIS
DIRECTORY SHOULD NOT EXIST PRIOR TO SETTING UP. THE SETUP SCRIPT WILL
ABORT IF IT DOES TO MAKE SURE YOU DON'T LOSE DATA.**

When you are done setting up the dropbox list and choosing the
repository, you should run the "setup-dropbox" script. This will make
sure the list is set up correctly and create and set up the
repository, making sure the certificate-protected web access, etc. is
set up.


Using
-----

To create a dropbox for someone, simply run "./create-dropbox
person". You can supply multiple people to create multiple
dropboxes. The script will create and set up a dropbox for them in the
repository and add them to the dropbox list. This will allow for the
following:

* Anyone on the dropbox list (i.e. you and anyone who has a
  dropbox) will be able to list the names of the people who
  have dropboxes, either from the shell or the web. In the
  default setup, the web URL will be
  https://web.mit.edu/$USER/dropbox/. The web access will be
  cert-protected and restricted to anyone on the dropbox list.

* Those who have a dropbox will be able to go to their dropbox
  and create/delete/edit/etc. files there (the only thing they
  can't do is grant permission to others). They will also have
  cert-protected web access at (in the default setup)
  https://web.mit.edu/$USER/dropbox/$person (where $USER is you
  and $person is them). You will also have both shell and web
  privileges to that directory (and you will also have the
  administer bit to change permissions in the directory).

* No one not on the dropbox list will be able to view anything
  in the dropbox repository, including the name of the
  dropboxes. No one except you will be able to view the
  contents of anyone else's dropbox.

To delete someone's dropbox, simply run "./delete-dropbox person". You
can supply multiple people to delete multiple dropboxes. This will
delete their dropbox and remove them from the list.