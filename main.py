# ეს ფუნქცია შედარებას აკეთებს ორ სორტირებულ ერეიზე (nums1 და nums2) და აბრუნებს მინიმალურ საერთო ელემენტს, თუ ის არსებობს, წინააღმდეგ შემთხვევაში კი -1-ს. i გამოიყენება nums1-ის ელემენტებისთვის, ხოლო j — nums2-ისათვის. თუ nums1[i] == nums2[j], ეს ნიშნავს, რომ მოვძებნეთ საერთო ელემენტი და უნდა დავაბრუნოთ nums1[i]. თუ nums1[i] < nums2[j], მაშინ i გავიტანთ წინ, რადგან nums1-ში უფრო პატარა ელემენტია და მას შემდეგ უნდა გავაგრძელოთ. თუ nums1[i] > nums2[j], მაშინ j გავიტანთ წინ, რადგან nums2-ში უფრო პატარა ელემენტია. თუ ციკლში ვერ მოვძებნით საერთო ელემენტს, მაშინ დავაბრუნებთ -1, რაც ნიშნავს, რომ ასეთი ელემენტი არ არსებობს.




class Solution(object):
    def getCommon(self, nums1, nums2):
        
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i] 
            elif nums1[i] < nums2[j]:
                i += 1  
            else:
                j += 1  
        
        return -1
