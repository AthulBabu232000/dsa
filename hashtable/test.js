const reverse=(s)=>{
    news=s.split('');
    console.log(news);
    length=s.length;
    console.log(length/2)
for(let i=0;i<length/2;i++){
    temp=news[i]
    news[i]=news[length-1-i]
    news[length-i-1]=temp 
    console.log(news[i],news[length-1-i]);
}
return news.join('');
}

result=reverse("welcome to javascript tutorials");
console.log(result);