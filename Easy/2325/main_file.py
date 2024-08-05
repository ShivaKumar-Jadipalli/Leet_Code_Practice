# class Solution:
#     def __init__(self):
#         self.Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#         self.encoding_dictionary = {'a' : 0 ,'b' : 0 ,'c' : 0 ,'d' : 0 ,'e' : 0 ,'f' : 0 ,'g' : 0 ,'h' : 0 ,'i' : 0 ,'j' : 0 ,'k' : 0 ,'l' : 0 ,'m' : 0 ,'n' : 0 ,'o' : 0 ,'p' : 0 ,'q' : 0 ,'r' : 0 ,'s' : 0 ,'t' : 0 ,'u' : 0 ,'v' : 0 ,'w' : 0 ,'x' : 0 ,'y' : 0 ,'z' : 0 }
#     def decodeMessage(self, key, message):
#         count =0
#         key = key.replace(" ","")
#         for i in key:
#             if self.encoding_dictionary[i]==0:
#                 self.encoding_dictionary[i]=self.Alphabets[count]
#                 count+=1
#         decoded_message = ''
#         for i in message:
#             if i != " ":
#                 decoded_message+=self.encoding_dictionary[i]
#             else:
#                 decoded_message+=" "
#         return decoded_message


class Solution: # well even after doing all this the time complexity just increased instead of decreasing 
    def decodeMessage(self, key: str, message: str) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        encoding_dictionary = {'a' : 0 ,'b' : 0 ,'c' : 0 ,'d' : 0 ,'e' : 0 ,'f' : 0 ,'g' : 0 ,'h' : 0 ,'i' : 0 ,'j' : 0 ,'k' : 0 ,'l' : 0 ,'m' : 0 ,'n' : 0 ,'o' : 0 ,'p' : 0 ,'q' : 0 ,'r' : 0 ,'s' : 0 ,'t' : 0 ,'u' : 0 ,'v' : 0 ,'w' : 0 ,'x' : 0 ,'y' : 0 ,'z' : 0 }
        count = 0
        for i in key:
            if i!=" ":
                if encoding_dictionary[i]==0:
                    encoding_dictionary[i]=alphabets[count]
                    count+=1
        dec_msg = ""
        for i in message:
            if i!=" ":
                dec_msg+=encoding_dictionary[i]
            else:
                dec_msg+=" "
        return dec_msg
print(Solution().decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))