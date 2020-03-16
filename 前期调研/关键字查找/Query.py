# 接口处已做注释  
# 默克尔树的部分hash函数里的m.update(item.encode('utf-8'))语句应当去掉，不然显示无法兼容bytes类型

from Tree import Tree

class QueryOneArtical:
    def query(self, key_words, text):
        sum = 0
        par_str = " ".join(self.data_to_text(self.byte_to_data(text)))
        for x in key_words:
            sum += self.find_str_begin(par_str, x)
        return sum

    def m_f_change(self, f_len, m, f, check_exits):
        if check_exits != -1:
            jump = f_len - check_exits
            m, f = m - f + jump, 0
        else:
            jump = f_len + 1
            m, f = m - f + jump, 0
        return m, f

    def find_str_begin(self, main_str, find_str):
        m, f = 0, 0
        m_len, f_len, result = len(main_str), len(find_str), list()
        while m < m_len:
            if main_str[m] == find_str[f]:
                m, f = m + 1, f + 1
                if f == f_len:
                    result.append(m - f_len)
                    flag = m - f + f_len
                    if flag > m_len - 1:
                        return len(result)
                    check_exits = find_str.rfind(main_str[flag])
                    m, f = self.m_f_change(f_len,m,f,check_exits)
                continue
            else:
                flag = m - f + f_len
                if flag > m_len - 1:
                    return len(result)
                check_exits = find_str.rfind(main_str[flag])
                m,f=self.m_f_change(f_len,m,f,check_exits)
        else:
            return len(result)

    def byte_to_data(self, final_byte):
        decode_01data = []
        for i in range(len(final_byte)):
            bb0 = final_byte[i]
            num = bb0[0]
            bb = bb0[1:]
            str0 = str(bin(int(bb.hex(), 16))[2:])
            if len(str0) % 8 != 0:
                extra0 = 8 - len(str0) % 8
                for j in range(extra0):
                    j += 0
                    str0 = '0' + str0
            str1 = str0[0: len(str0) - num]
            decode_01data.append(str1)
        return decode_01data

    def cmp_ok(self, a, b):
        l = len(b)
        k = 0
        if len(a) < len(b):
            return False
        while k < l:
            if a[k] == b[k]:
                k += 1
            else:
                return False
        return True
    
    def data_to_text(self, decode_01data):
        global code_dict
        result = []
        for i in range(len(decode_01data)):
            result_part = ""
            uncompress_code = decode_01data[i]
            while len(uncompress_code) > 0:
                for j in code_dict:
                    if self.cmp_ok(uncompress_code, code_dict[j]) == True:
                        h = len(code_dict[j])
                        uncompress_code = uncompress_code[h:]
                        result_part += j
            result.append(result_part)
        return result


if __name__ == "__main__":
    key_words = input('input a list of key words ：').split(' ')
    while len(key_words) < 3:
        key_words = input('the number of key words should more than 2：').split(' ')

    # ---------------------------测试用例区--------------------------------
    # 先建一个默克尔树用来测试
    tree=Tree()
    # 每个区块对应的字典序(到时换成区块中存的字典)
    code_dict = {'L': '10000111010', 'A': '10000111011', '8': '10000111000', '7': '10000111001', 'S': '110111001010', 'x': '110111001011', 'B': '11011100100', '5': '0000110110', 
    'P': '0000110111', "'": '0000110100', '4': '0000110101', 'W': '1000010010', 'I': '1000010011', '9': '1000010000', '—': '1000010001', '-': '1101110011', '3': '1101110000', 
    'C': '1101110001', '2': '1000011110', 'z': '1000011111', '"': '110100110', 'k': '110100111', 'M': '110100100', '0': '110100101', '1': '00001100', 'G': '10000101', ',': '10000110', 
    'v': '11011101', 'O': '11011110', '.': '11011111', 'T': '0000111', 'b': '1101000', 'w': '000010', 'g': '100000', 'f': '101010', 'u': '101011', 'p': '110101', 'y': '110110', 
    'm': '00000', 'c': '10001', 'd': '10100', 'l': '11000', 'h': '11001', 'r': '0001', 's': '0100', 'i': '0101', 'n': '0110', 'a': '0111', 'o': '1001', 't': '1011', 'e': '001', ' ': '111'}
    # 默克尔树每个叶节点对应的数据块，以列表的形式存入
    # 测试用例
    text = [b'\x06\x0f\x93\xc3\xce\x9fi\xf0\xf6\x96\x1e\xd2\xfd\xecl\rV)\xeeF9\xf8X3j\xd0x\x91 \x96\xdb\xabwh\xa9k\xfb\xd8\xd8\x1a\xab\xf0\x97\x18\xfa\x0f\xbc\x9fR\x8a_V\xe0\x91>\xf2\xed\xf7\x00\xdb\xec\\S\xdc\xfd\x07\xe4\xe2\x9c%\xbc\xcdw\xd3S\x1b{\x91N\xf5Y\x1f#\x03\xb2\xc3\xe4S\xcb}$\xb5\x1fn\xadc4\xae&\x9e\xd6\x0c\xd9\x1e\x02\xe9X\x94\xf7?Q\x9b1\xbe\xf0:\xb2_\xbc\x9f\x19\x19g\xddQ\xad7\xc0', 
    b'\x01\x85\x12bCD\xfb\xd8\xd8\x1a\xac~\xe3 \x02\xdd\x93\xd1\xd6\x9d51\xb7\xb9\x14\xe1Mx\xa7\xd0y\xdc\xb8\xe2\xba\x1az\x86A\xf4M\xe7\xdeO\xa0\x94N\'%\xc5\x1f\x1d\xef\xdeOv\x8a\x96\xbe\x8bg\xcbxH\xd1\x8aQ\xf6\xee\xd4\xf7\x93\xc2Z\x1cm\xf4\x0c\xbd"\xe9~$H%\xb6\xf2\xdc>k\x14\xa3\xed\xbe', 
    b'\x07\x0f\x95N\xa9\xef\'\xd4\xa2\x97\xed@z+D\xfb\xc9\xe1\x90\x848\r|:\x94\xf0\xed\xa08)\xf7\xb1\xb05X\xa7\xbc\xbd\xfb\xc9\xf1"A-\xb7\tq\x8f\xa0\xfc\x9cS\x84\xb7\x99\xae\xfb\xb6\xdd51\xb7\xb9\x14\xf8\x9a\xda\x05h<\xb7\xbc\x9f\x00\xba&\xdd1:\x94\xf3W\xbc\x9e\xed\x15-}-\xe8\xb5\x83\xab{\xc9\xf6\xad\xb7\r\xce\'Yb\x8a\xed\xf2\xe0\xc1\xbd\xfe\x1f\'\xc4\x89\x04\xb6\xde\x11\xf98\xa7\xd17\x9fT\x8fJ\xc0\x02=\xda\x9c%k#\xe1\\\x05<#\xebJ\xdf\x18\xdb\xbd\xd8\xbcm:\x1d\xd2/\x8fy\x9a\xd1\xda\x9d51\xb7\xb9\x14\x86\xea\xd1\xc5tV\x83\xc2\x89:t\xee\xd4\xf5H\x95\x81\xbe\xea\xa2\xdc\x8ao\x80', 
    b"\x01\xd3\x07\xc9\xf8X3j\xd0x\x91 \x96\xdb\xcd^\xf2~\xf66\x06\xab\x1fV\x1c\x07\x84\xb8\xc7\xd0}%\x8f\to3]\xfb\xc9\xfa\x89B\xd1>j\xe9\xa9\x8d\xbd\xc8\xa7v\xa7\x96\xc6\xdc3K\xa5\xea\xdb\xabf\x9d\xda\x9d\xe3\x114[4\xf0VR\xd2\x1bM\xef\'\xc2\x89:\x7f\xbd\x8d\x81\xaa\xc7\xee2\x00-\xd9=\x1di\xd5\xbb\xf4\xb7\xb2\x02\xd7\xbe", 
    b'\x04\xd3\x07\xc9\xf4\x12\x89\xc4\xe4\xb8\xa3\xe3\xcb}#\x8cs\xc3\x038K\x8c}\x07\xc7\x12\x86\x9e\xe7\xa6\xa66\xf7"\x9d\xda\x9c\x06\x8a\xfb\xfa`', 
    b"\x04\x0f\x93\xf7\xb1\xb05X\xfb\x91\x8exK\x8c}\x07\xe1o\xab}\xecl\rU\xfb\xdf~\x91|\x1ant\x90\x9b\xc4\x89\x04\xb6\xde[\xe9\x1cc\x9e\x19\x0f}\x06\xa9\x13\xdf\xa1\xdd-\xb9\xd1\xf6\xe2p\xfb{\xcb\xdf\x8dx\x02\xb3\xd9N\x12\xde{\xfc\xbbRwH\xf8\x91 \x96\xdb\xabxQ&\'\xcb}#\x8cs\xc3!\r\xf0", 
    b'\x06\x0f\x93\xda\xb0h#\xe6\xaf\xa9\x9dpz\xb2-\x0f\xbc\x9e\xed\x15-}-\xe8\xb5\x83\x84\xb8\xc7|$\xfd\x07\x89\xa5q4\xe1-\xe7\xcbcn\xfe\xa2\x17\xa4\xc3\xe5\xb8\x9dD\xa1k{]\xd2\x9ej\xf7\x93\xc3\xce\x9fi\xf0\xae\x02\x9e\xa1\x90w\xf0\x0c\xd7\xaf\x9a\xbb\xe8\x9a\xef\x86\x06\xda^\xf8\xc4\x84i\xde1(\x9e\xe7\xdeO\x89\x12\tm\xb7\xc0', 
    b'\x01\xde\x18\x1d\x96\x1f"\x9c%\xc6;\xe1\'\xa6k\xbfy?Q(\x9e%\xac\x8f\xaaq\x89\tZ\x0fy>$H%\xb6\xf7=\xf7ei\xef\'\xc0\xf7\x92*\xd0y\xab\x81\xdbo\xa9\x9dpz\xb7v\xea\xd4\x99\x1e\xe2_\xbbS\x84\xb8\xc7Kx\x0f\x84\x8d\x18\xa5\x1f`\xd1=\x04\xa2q9.(\xf8\xe1-\xe6k\xbfy?Q(Z\'\xcd\\\x06\x8a\xfb\xfc<\xe9\xf6\x9f\x97\xa7|\tzm\xd2\xe7]M>\xe0\x1a\xe9|r\xb8\xa0\x96\xf5\x0c\x83\xbd\xd9j+A\xbe', 
    b'\x06\x85\x12b|\xb7\xdc\xaa\xda\x8f\xb7vi\xad\xa2i\xdf\xd8S\xb9\x84N\x9f\xe8v\xf2\xdd5\x91\xb5h9\xdd-i\xc2[\xcfMLm\xeeE;\xb5<\xb7H\xe6g\x1e\xa58\xa7\xb1]R\x1b\xbau\xb4\xedX4\x11\xf3W\x8c\x8c\xb3\xee\xa8\xd6\x9e.\x858\xca\x1f\xa3n\x87t\xb7\xb9\xf0\xe7p\xdf\xe1\xf2~\xa2j1\xba\xc4\xf9\xab\xc2xW\x86\xf3W\x0b+\x1c\xfd\xecl\rU\xfa\xa7\xd5\xc6\xe1\xba\xa7pKA\xdcK\xa7\x9a\xbd\xe4\xf8\xcdmc\xb7\xcb\x8d\n_\xca\xdf\xd1\xb7\xbc\x9f\x19\x19g\xddQ\xad7\xc0', 
    b'\x03\x0f\x93\xf4\x8f\xb4\x8f\x9a\xbe\xf66\x06\xaa\xff.\x9c![\xb2\xde\xe7\xc2mdY\xede\x9f\x1f{\x1b\x03U\x8f\xdcd\x00[\xb2xn%\x16\x85\xaf\x87\xcc\x81\xd3\xeeG\x8ea\xbe\xa3:\xca+A\xef\'\xeb)z\xcb\x10\x16\xbf5{\xc9\xf1"A-\xb7\xad\xadq\xf4\x8f\xb6\xf8', 
    b"\x01\xd3\x07\xc9\xf4v\x80\x8f\x9a\xba[\xc0\xad\x07\xbc\x9fr1\xcf\xc2\xc1\x9bV\x83\x84\xb7\x9f-\x8d\xbb\xfc\xbbR\xaa\xf1\xe6\xae\x9a\x98\xdb\xdc\x8aC|(\x16\xcd;V\r\x04|\xd5\xe6\xaa\x96*\xf8N\xedOC\x83\x03\xda\xcb$7v\xa7\xad\xa8G\xbf\x8e&\xbay\xab\xd4\\{\xb5<e\xa2E\xb8K\x8cz8\x1e\x03\xef\'\xc0%\xed\x8a\'v\xa7\xd4JZ\xc0|\xd5\xef*\x9c\xee\x96\xb8m7\xde\xc6\xc0\xd5_\x81\xf6\x91\xf0\xab#\x04\xa7\x8520,\xeb5\xe2S\xa3\xad:\xb7\xca\xa7\xc1\xbb#\xbe"]
    root=tree.creat_leaf_node(text)  
    artical=[]
    tree.get_artical(root, artical)
    #----------------------------------------------------------------------
    query01 = QueryOneArtical()
    sum01 = query01.query(key_words, artical)
    print('关键词组在当前文章里出现的次数为：' + str(sum01))
    