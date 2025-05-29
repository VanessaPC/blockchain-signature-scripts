### Generate extended pubkeys and bech32 for Cardano Byron era addreses

#### In order to do get the bech32 required:

1 - Paste you `skey` in the `./toBech32.py`
2.- Run `python ./toBech32.py`

This will produce the following output:

```py
ed25519_sk1ap8naeff3jcle2zlqpmfjffpp6829atzhxnwxw82p4k9dty3lgq6gq95tqrs97lwl0uljuxvn5rmmne8d2uclyn3nelztzq36r3283rx4dgp63qyyc65cg4jps9h5n7qfq82qcmp6tas5vlawwfp0eh5wgcyflcp
```

Where you run your cardano-signer, save it to an `.skey` file.

```
echo "ed25519_sk1ap8naeff3jcle2zlqpmfjffpp6829atzhxnwxw82p4k9dty3lgq6gq95tqrs97lwl0uljuxvn5rmmne8d2uclyn3nelztzq36r3283rx4dgp63qyyc65cg4jps9h5n7qfq82qcmp6tas5vlawwfp0eh5wgcyflcp" > sign.skey
```

#### Generate your extended pub key of your vkey

1.- Paste your `vkey` in the file `extendedpubkey.py`
2.- Run `python ./extendedpubkey.py`

It will generate the following:

```
Public Key  : c6597fdb8d0c72485be8ae8def9e582fa12632297a097f8b2a6c198b90f7b68d
Chain Code  : 66ab501d440426354c22b20c0b7a4fc0480ea06361d2fb0a33fd739217e6f472
Extended Pub Key (raw): c6597fdb8d0c72485be8ae8def9e582fa12632297a097f8b2a6c198b90f7b68d66ab501d440426354c22b20c0b7a4fc0480ea06361d2fb0a33fd739217e6f472
```

You need the extended pub key to paste where the GD form says 'Paste extended pub key'.

#### Use your cardano-signer to generate a signature

```
cardano-signer sign --data "STAR 68 to message" --secret-key sign.skey --json-extended
```

Use the signature part to paste in the glacier drop.
