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

https://ithelp.ithome.com.tw/articles/10300062