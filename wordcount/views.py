from django.shortcuts import render

# Create your views here.

def home(request) :
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()  
    word_dictionary={}
    for word in words :
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1         
   
    

    
    word_most=sorted(word_dictionary.items(),key=lambda t:t[1])  #value 값을 기준으로 오름정렬..
    # =sorted(word_dictionary.items())
    wordmostone,y = max(word_dictionary.items(),key=lambda t:t[1])  # key 값을 기준으로 찾아.

    # x,y = max(word_dictionary)

    
    #순서 정렬하기
    


    # return render(request, 'result.html',{'full':text, 'total':len(words), 'dictionary':word_dictionary.items(), 'word_most':word_most})
    
    context = {'full':text, 'total':len(words), 'dictionary':word_dictionary.items(), 'word_most':word_most, 'wordmostone':wordmostone}
    return render(request,'result.html',context)
    



    
 