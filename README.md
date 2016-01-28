# Retropie Administrator
A little web-service for administrate the RetroPie process using Python libraries.

![Screenshot](https://github.com/matisanh/retropie-administrator/blob/master/Screenshot.png)

## Installation

First, you should have [RetroPie](https://github.com/RetroPie) already installed. There's an awesome guide to do so right [here](https://github.com/RetroPie/RetroPie-Setup).

Installing an FTP server is optional, but recommended. If you don't know how to do that, you can do it like so:

```bash
sudo apt-get install vsftpd
```

You should be able to access your Raspberry Pi using FTP. I recommend you to create a `retro` user like this:

```bash
# Create the retro user.
sudo useradd retro
sudo passwd play

# Set the default home folder.
chroot_local_user=YES
sudo usermod --home /home/pi/RetroPie/roms retro

# Restart the service for changes to make effect.
sudo service vsftpd restart
```

Install the administration web interface cloning this repository and adding an entry to the `crontab` list:

```bash
# Clone Retropie Administrator into the home folder.
git clone git://github.com/matisanh/retropie-administrator ~/RetroPie

# Schedule the launcher command.
crontab -l | { cat; echo "@reboot sh ~/RetroPie/launcher.sh > ~/RetroPie/cronlog 2>&1"; } | crontab -
```

## Usage

Installing ROMs is pretty easy. Just FTP into your Raspberry Pi's with your username and password (you just created them in the Installation step).

Use your browser to open `http://your-raspberry-pi:8080`. It's possible to change the default port (8080) to one of your own editing the `main.py` file.

## Development

Pull requests are welcome and mostly appreciated.

## Credits

Copyright and License of the Free Lancer - by Start Bootstrap Theme

Copyright 2013-2015 Iron Summit Media Strategies, LLC. Code released under the [Apache 2.0](https://github.com/IronSummitMedia/startbootstrap-freelancer/blob/gh-pages/LICENSE) license.
