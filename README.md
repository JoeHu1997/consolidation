# consolidation
calculate consolidated clay  
階段一：完成壓密函數  
階段二：將其包裝成有完整流程的應用程式，若有介面會更好  
階段三：將其部署至網頁上，但可能會牽扯到前端與程式語言  
Stage One: Implementing the compression function.  
Stage Two: Packaging it into a complete application with potential interface improvements.  
Stage Three: Deploying it on a webpage, possibly involving frontend and programming language considerations.  
以下為思考過程：
常見的壓密問題圍繞在應力、沈陷量、以及壓密時間三個部分，因此要完成整體的問題求解，需要先得到完整的土壤參數．  
以顧問公司的角度，這些參數委外的時候通常都會得到，而以考生的角度，通常不會將所有參數給齊，所以會發生需要利用公式推導的情形發生，故土壤參數階段，會需要建立各種不同的參數轉換的函數．常見提供的物理量為：土壤的某種密度、孔隙率、孔隙比、比重、含水量．這幾者之間要能完全轉換．後續進行計算時，主要會利用到的參數土壤的濕密度，土壤乾密度為最常見的參數．  
土壤參數的建立過程，為了避免逐次檢查每個參數，可以利用while迴圈並搭配missing_params，便可在參數皆完善的時候跳出迴圈．所以利用這個方法的話，越基本的參數需要被放在迴圈的最前面．  

12/06 經過昨日與大神的探討，決定將開發的部分，與後端建立一起開發，目前選定的後端框架為flask，若不考慮程式的擴充性，可以利用submit多個土壤參數的方式，將資料傳至專門計算的route，並再回傳計算結果。
12/07 flask的範例專案為會員系統登入，其結構為輸入兩組數字作為帳號密碼，並進行判斷．  
應用在我們的專案，提交的部分為各種土壤參數，而原本連接至資料庫的部分，則替換為utility functions，登入成功的頁面則替換為計算的結果．  
前四項土壤參數換算已完成，再來就是推廣到七參數中使用，gammad、gammas跟gammam皆可以用前四個參數及水密度進行計算，主要要分析題目所提供的參數是否皆有方程式可以找到相關性。  
Gs* w = S*e(4)  
gammad = Gs* gammaw/(1+e)(3)  
gammam = Gs* gammaw*(1+w)/(1+e)(4)  
#gammas = Gs*gammaw(2)  
三個方程式 六個未知數 至少要有三個已知 因此未知的情況為C6取3 20種組合:  
(1)若三個已知為Gs* w = S*e中的三個 可視為第一種情形(4) =>gammad,gammam必為未知  
(2)gammam = Gs* gammaw*(1+w)/(1+e) 同上(4)與上面有一個重複=>gammad必為未知  
(3)gammad = Gs* gammaw/(1+e) 這三種則必須再多知道一個第一式中的未知數 (6)+(6)=> gammam必為未知且此三個參數同時為已知並無解出方程式．
判斷流程： 
1.gammad,gammam皆為未知   
2.若gammad為未知  
3.若gammam為未知且gammad,Gs,e其一為未知  
4.若gammam為未知且gammad,Gs,e皆為已知  

12/12  
基本參數的計算已完成，前端模板先用chatgpt的生成內容將就使用，接下來目標就是建立壓密函數．  
壓密函數主要計算流程再建立完土壤基本參數後，就是進行有效應力的計算，可以分為：  
    (1)純黏土
    (2)沙土壓黏土
    (3)沙土壓黏土壓沙土
除了土層外，通常題目會伴隨著地下水面下降後會如何改變，此過程就會產生壓密．以及最後有時會出現外加載重的情況，也要一併考慮．
故函數開發第二階段期望建立各種情況下的壓密沈陷量的計算即可．

參考資料：
https://ithelap.ithome.com.tw/articles/10300062