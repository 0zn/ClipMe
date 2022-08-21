# ClipMe
A Persistent Bitcoin Address Clipper

# About

A "Clipper" is a type of malware that targets cryptocurrency transactions.
When users copy the address of a wallet that they intend to send Bitcoin to, the copied address is stealthily replaced by (you) the attacker's.
This is to demonstrate the evolution of malware in the current crypto age. 
The script should not, at the moment, be detected by any sort of antivirus.

# Features
 

    No external Python modules required
    HIDE
    AUTO STARTUP (REGISTRY ENTRY)

The script will add itself to startup through the registry to ensure that it runs persistently.

# Use


    Change "YOUR ADDRESS HERE" to your wallet address.
    Run -> python clipper.pyw

# Disclaimer

This is intended for EDUCATIONAL PURPOSES , I am not reponsible for any malicious activity of others.
For non technical users, the script is relatively harmless to test/run on your machine, however it is always good practice to use a Virtual Machine.
For removal, you only need delete the script + the registry key located in `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`.

# TODO

    Self replication to %AppData%
    Self destruct
    Add to PATH
    Persistence for Mac
    Linux Support
