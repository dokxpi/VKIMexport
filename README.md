## VKIMexport :boom: (0.1.3)

VKIMexport — это скрипт на Python, для скачивания фотографий из бесед или диалогов интересующего вас собеседника социальной сети [vk.com](https://vk.com)

![Fisher](https://raw.githubusercontent.com/dokxpi/VKIMexport/master/publish/cmd.main.py.gif)

[Список изменений] (https://github.com/dokxpi/VKIMexport/blob/master/changes.md)
***
**Требования:** Python 3.3.6 [+]
***
####Текущие проблемы и статус####
📌 Внимание: скрипт временно не работает (проблемы с авторизацией)
***
#### Как пользоваться?
В первую очередь нам потребуется установить сам python и дополнительные к ему библиотеки:
* скачиваем с официального сайта интерпретатор ```www.**python**.org``` и устанавливаем его <br/>
   ([загрузить] (https://github.com/dokxpi/VKIMexport/blob/master/toolbox/-%20python/python-3.4.2.amdx86-64.rar?raw=true) для windows)
* скачиваем с сайта ```www.lfd.uci.edu/~gohlke/pythonlibs``` установщики библиотек *lxml*,*requests* и устанавливаем их
   ([загрузить] (https://github.com/dokxpi/VKIMexport/blob/master/toolbox/-%20library/lxml&requests.rar?raw=true) для windows)

> **Обратите внимание**
<br/>
Разрядность программ (установщиков) должна соответствовать разрядности установленной версии Python, в противном же случае вам придется указывать пути самостоятельно ([определить сейчас] (http://dokxpi.github.io/VKIMexport/))
 
* подключаем ```pip``` ([загрузить] (https://github.com/dokxpi/VKIMexport/blob/master/toolbox/-%20pip/pipwin.rar?raw=true) для windows) 


* запускаем командную строку (windows: открыть диалог «Выполнить» с помощью сочетания клавиш  ```Win + R``` и введите ```cmd```  –> нажмите OК) и в появившемся окне консоли, выполним следующие команды 
 *  **```cd C:\Python34\Scripts```** и жмем клавишу ```ENTER```/ - где ```\Python34\``` версию вашего интерпретатора
 *  **```pip install cssselect```** и жмем клавишу ```ENTER```/ 

*** 
Теперь мы готовы к запуску VKIMexport, но перед тем как запустить нам потребуется узнать значение переменой ```DIALOG_ID```, для этого 
* перейдите по адресу ```https://vk.com/im```
* выберите интересующий вас диалог и кликнете на нем мышкой
* скопируйте значения **```set```** в адресной строке вашего браузера ![set](https://raw.githubusercontent.com/dokxpi/VKIMexport/master/publish/vkset.png)  
   - где *"69828681"* значение переменной ```DIALOG_ID```

* [загрузите скрипт VKIMexport] (https://github.com/dokxpi/VKIMexport/blob/master/toolbox/-%20releases/v0.1.3/main.zip?raw=true) на ваш компьютер и распакуйте его содержимое в корень диска **```C:```** (убедитесь в доступности скрипта по адресу```C:\main.py```)
* откройте файл ```main.py``` в [текстовом редакторе] (http://notepad-plus-plus.org/) и отредактируйте в нем следующие переменны
  
 ![txt](https://github.com/dokxpi/VKIMexport/blob/master/publish/main.py.png?raw=true)
          
#### Запуск
Вызвать командную строку (windows: открыть диалог «Выполнить» с помощью сочетания клавиш  ```Win + R``` и введите ```cmd```  –> нажмите OК) и в появившемся окне консоли, выполнить команду
* **```C:\Python34\python.exe C:\main.py```**  

Вот и всё!

*** 
Остались вопросы?<br/>
Создайте [issue](https://github.com/dokxpi/VKIMexport/issues) в репозиторий или [свяжитесь](http://dokxpi.github.io) со мной!
