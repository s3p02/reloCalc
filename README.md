# Reloc. Calc.

On VM

```sudo yum install -y git```

```git clone https://github.com/s3p02/reloCalc.git```

```cd reloCalc```

```bash vm-install.sh```

```which python3```

```virtualenv -p /PATH/TO/bin/python3 py3env```

```source py3env/bin/activate```

```pip install requests```

```mkdir data```

VM E2 16 vCPU - pool(32)
real    1m0.743s
user    1m55.490s
sys     0m7.526s

VM N1 HIGH CPU 16 - pool(32)
real    1m7.973s
user    1m53.171s
sys     0m8.298s

VM e2-highcpu-16-us-west1-b - pool(32)
real    1m1.434s
user    1m52.471s
sys     0m7.010s
