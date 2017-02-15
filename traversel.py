# data = {'count': 2,
#         'text': '1',
#         'kids': [{'count': 3,
#                   'text': '1.1',
#                   'kids': [{'count': 1,
#                             'text': '1.1.1',
#                             'kids': [{'count':0,
#                                       'text': '1.1.1.1',
#                                       'kids': []}]},
#                            {'count': 0,
#                             'text': '1.1.2',
#                             'kids': []},
#                            {'count': 0,
#                             'text': '1.1.3',
#                             'kids': []}]
#                 },
#                  {'count': 0,
#                   'text': '1.2',
#                   'kids': []
#                   }
#                   ]}

data1 = [
      {'child': 
        {'kids': [
              {'child': 
                {'kids': [
                      {'child': {'kids': [], 
                           'type': 'file', 
                           'name': 'custom'
                           }
                      }
                    ], 
                'type': 'folder', 
                'name': 'js'
                }
              }, 
              {'child': {'kids': [], 
                    'type': 'folder', 
                    'name': 'css'
                    }
                }, 
              {'child': {'kids': [], 
                    'type': 'folder', 
                    'name': 'css'
                    }
                }
            ], 
        'type': 'folder', 
        'name': 'html'}
      }, 



      {'child': 
        {'kids': ['js', 'css', 'img'], 
        'type': 'folder', 
        'name': 'angular'}
      }
    ]


data = data1[0]

def traverse(data):
    print "~~~~~"
    # print data

    # if data['text']:
    # if 'child' in data:
        # print data['child']['name']
        # print "~~~~~~~~" ,data['child']['name']
    # print ' ' * traverse.level + data['child']['name']
    # path = []
    p = ""
    for kid in data['child']['kids']:


        traverse.level += 1
        traverse.level -= 1
        print kid['child']['name'] 
        p = kid['child']['name']
        if len(kid['child']['kids']) > 0:
            p = p + kid['child']['name'] 
            traverse(kid)
        else:
          traverse.path.append(p)
          p = ""

    print traverse.path

if __name__ == '__main__':
    traverse.level = 1
    traverse.path = []
    traverse(data)