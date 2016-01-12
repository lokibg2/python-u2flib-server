YUBICO = {
    "identifier": "2fb54029-7613-4f1d-94f1-fb876c14a6fe",
    "version": 3,
    "vendorInfo": {
        "url": "https://yubico.com",
        "imageUrl": "https://developers.yubico.com/U2F/Images/yubico.png",
        "name": "Yubico"
    },
    "trustedCertificates": [
        "-----BEGIN CERTIFICATE-----\nMIIDHjCCAgagAwIBAgIEG1BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZ\ndWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAw\nMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290\nIENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK\nAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk\n5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep\n8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbw\nnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT\n9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXw\nLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJ\nhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjAN\nBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4\nMYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kt\nhX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2k\nLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1U\nsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqc\nU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw==\n-----END CERTIFICATE-----"
    ],
    "devices": [
        {
            "deviceId": "1.3.6.1.4.1.41482.1.1",
            "displayName": "Security Key by Yubico",
            "deviceUrl": "https://www.yubico.com/products/yubikey-hardware/fido-u2f-security-key/",
            "imageUrl": "https://developers.yubico.com/U2F/Images/SKY.png",
            "selectors": [
                {
                    "type": "x509Extension",
                    "parameters": {
                        "key": "1.3.6.1.4.1.41482.1.1"
                    }
                },
                {
                    "type": "x509Extension",
                    "parameters": {
                        "value": "1.3.6.1.4.1.41482.1.1",
                        "key": "1.3.6.1.4.1.41482.2"
                    }
                }
            ]
        },
        {
            "deviceId": "1.3.6.1.4.1.41482.1.2",
            "displayName": "YubiKey NEO/NEO-n",
            "deviceUrl": "https://www.yubico.com/products/yubikey-hardware/yubikey-neo/",
            "imageUrl": "https://developers.yubico.com/U2F/Images/NEO.png",
            "selectors": [
                {
                    "type": "x509Extension",
                    "parameters": {
                        "key": "1.3.6.1.4.1.41482.1.2"
                    }
                },
                {
                    "type": "x509Extension",
                    "parameters": {
                        "value": "1.3.6.1.4.1.41482.1.2",
                        "key": "1.3.6.1.4.1.41482.2"
                    }
                }
            ]
        },
        {
            "deviceId": "1.3.6.1.4.1.41482.1.3",
            "displayName": "YubiKey Plus",
            "deviceUrl": "https://www.yubico.com/products/yubikey-hardware/",
            "imageUrl": "https://developers.yubico.com/U2F/Images/PLS.png",
            "selectors": [
                {
                    "type": "x509Extension",
                    "parameters": {
                        "key": "1.3.6.1.4.1.41482.1.3"
                    }
                },
                {
                    "type": "x509Extension",
                    "parameters": {
                        "value": "1.3.6.1.4.1.41482.1.3",
                        "key": "1.3.6.1.4.1.41482.2"
                    }
                }
            ]
        },
        {
            "deviceId": "1.3.6.1.4.1.41482.1.4",
            "displayName": "YubiKey Edge",
            "deviceUrl": "https://www.yubico.com/products/yubikey-hardware/",
            "imageUrl": "https://developers.yubico.com/U2F/Images/YKE.png",
            "selectors": [
                {
                    "type": "x509Extension",
                    "parameters": {
                        "value": "1.3.6.1.4.1.41482.1.4",
                        "key": "1.3.6.1.4.1.41482.2"
                    }
                }
            ]
        },
        {
            "deviceId": "1.3.6.1.4.1.41482.1.5",
            "displayName": "YubiKey 4/YubiKey 4 Nano",
            "deviceUrl": "https://www.yubico.com/products/yubikey-hardware/yubikey4/",
            "imageUrl": "https://developers.yubico.com/U2F/Images/YK4.png",
            "selectors": [
                {
                    "type": "x509Extension",
                    "parameters": {
                        "value": "1.3.6.1.4.1.41482.1.5",
                        "key": "1.3.6.1.4.1.41482.2"
                    }
                }
            ]
        }
    ]
}
