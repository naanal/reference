
# SAN Configuration


```python
apt-get install git
```


```python
git clone https://github.com/naanal/reference
```


```python
cp -a reference/openstack/cinder/dothill /usr/lib/python2.7/dist-packages/cinder/volume/drivers/
cp -a reference/openstack/cinder/interface /usr/lib/python2.7/dist-packages/cinder/
cp -a reference/openstack/cinder/hp_msa /usr/lib/python2.7/dist-packages/cinder/volume/drivers/san/
cp reference/openstack/cinder/exception.py /usr/lib/python2.7/dist-packages/cinder/
```


```python
source ~/openrc
cinder type-create hpmsa
cinder type-key hpmsa set volume_backend_name=hpmsa-array
```

modify /etc/cinder/cinder.conf with reference to http://docs.openstack.org/liberty/config-reference/content/hp-msa-driver.html and example_cinder.conf


```python
service cinder-volume restart
```
