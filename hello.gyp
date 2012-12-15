  {
    'targets': [

     {
        'target_name': 'foo',
        'type': 'executable',
        'sources': [
          'foo.cc',
        ],
        'dependencies': [
           'new_library'
        ]
      },

      {
        'target_name': 'new_library',
        'type': '<(library)',
        'defines': [
          'FOO',
          'BAR=some_value',
        ],
        'include_dirs': [
          '.',
        ],
        'sources': [
          'src/new_library.cc',
        ],
      },
    ],
  }
