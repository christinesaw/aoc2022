input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

from pprint import pprint

input_list = input.split('\n')
pprint(input_list)

mky_dict = {}

for each in input_list:
    if each[0:6] == 'Monkey':
        mky_num = each[7:]
        mky_dict[mky_num] = []
    if each[2:16] == 'Starting items':
        worry_levels = each[17:].split(',')
        worry_levels = [int(ii) for ii in worry_levels]
        mky_dict[mky_num] = worry_levels
        print(worry_levels)
        # mky_dict[mky_num].append()

pprint(mky_dict)

class Monkey:
    def __init__(self,name):
        self.name = name
        self.items = []
        self.op = ''
        self.test = 0
        self.test_true = 0
        self.test_false = 0
    
    def assign_items(self,in_list):
        self.items = in_list
    
    def add_items(self,item):
        self.items.append(item)
    
    def assign_test(self,test_num):
        self.test = test_num

    def assign_test_true(self,mky):
        self.test_true = mky
    
    def assign_test_false(self,mky):
        self.test_false = mky

    def assign_op(self,op):
        self.op = op
    
    def run_test(self, item):
        if item % self.test == 0:
            return True
        else:
            return False

    def remove_item(self,item):
        self.items.remove(item)

    def __str__(self):
        return ("{} has items {}, true mky is {}, false mky is {}".format(self.name, str(self.items), self.test_true, self.test_false))


current_mky = ''
mky_list = []

for each in input_list:
    each = each.strip()
    if each[0:6] == 'Monkey':
        mky_num = each[7:].strip(':')
        name = 'mky' + mky_num
        mky = Monkey(name)
        mky_list.append(mky)
        current_mky = mky
    
    elif each[0:14] == 'Starting items':
        items_list = each[16:].split(',')
        items_list = [int(ii) for ii in items_list]
        current_mky.assign_items(items_list)
    
    elif each[0:4] == 'Test':
        test_num = int(each[19:])
        current_mky.assign_test(test_num)

    elif each[0:7] == 'If true':
        true_mky = 'mky' + each[25:]
        current_mky.assign_test_true(true_mky)

    elif each[0:8] == 'If false':
        false_mky = 'mky' + each[26:]
        current_mky.assign_test_false(false_mky)



    


for each in mky_list:
    print(each)

# mky_list[0].remove_item(98)
# print(mky_list[0])