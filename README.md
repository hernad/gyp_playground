# GYP playground

## Mac

create xcodeproje:

     gyp hello.gyp -D library=shared_library --depth 1


build:

     gyp_playground$ xcodebuild -project hello.xcodeproj -configuration new_library


### Mac via Sconstruct

Može se generisati i SConstruct sa gyp-om:

    GYP_GENERATORS=scons gyp --depth . -D library=shared_library
    brew install scons
    scons


## dylib open

export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:`pwd`

