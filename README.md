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
前四項土壤參數換算已完成，再來就是推廣到六參數中使用，gammad跟gammam皆可以用前四個參數及水密度進行計算，主要要分析題目所提供的參數是否皆有方程式可以找到相關性。

參考資料：
https://ithelap.ithome.com.tw/articles/10300062