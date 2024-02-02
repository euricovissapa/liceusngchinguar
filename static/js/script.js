
$(document).ready(function(){
    if(document.querySelector('.btn-danger')){
        let botao = document.querySelectorAll('.btn-danger');
        for(i=0; i<botao.length;i++){
            botao[i].addEventListener('click', function(event){
                if(confirm('Tem certeza que deseja eliminar este registo ?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            })
    }
    }
    })

(function(win,doc){
    'use strict';

    if(doc.querySelector('#form')){
        let form = doc.querySelector('#form');
        function sendForm(event){
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN', token);
            ajax.send(data); 
            ajax.onreadystatechange = function(){
                if(ajax.status === 200 && ajax.readyState === 4){
                    let result = doc.querySelector('#mensagem');
                    result.innerHTML = 'Operação realizada com sucesso!';
                    result.classList.add('alert');
                    result.classList.add('alert-sucess');
                }else{
                    let result1 = doc.querySelector('#mensagem');
                    result1.innerHTML = 'Operação mal sucedida!';
                    result1.classList.add('alert');
                    result1.classList.add('alert-danger');
                }
            }
        }
        form.addEventListener('submit', sendForm, false);
    }

})(window,document)
