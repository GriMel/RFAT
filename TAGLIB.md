Taglib installation instructions
================================
[Source](http://www.linuxfromscratch.org/blfs/view/svn/multimedia/taglib.html)
* wget https://taglib.github.io/releases/taglib-1.11.tar.gz
* tar -xvf taglib-1.11.tar.gz
* cd taglib-1.11
* cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release  -DBUILD_SHARED_LIBS=ON
* make
* **sudo** make install