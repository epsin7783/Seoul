/*게시판용*/
/*스크립트는 끝나는 부분은 ; 을 작성해라*/
var writererror = "작성자를 입력하세요";
var subjecterror = "글제목을 입력하세요";
var contenterror = "글내용을 입력하세요";
var passwderror = "비밀번호를 입력하세요";

$(document).ready(
	function(){
		//글쓰기용
		$("form[name='inputform']").on(
			"submit",
			function(event){
				if(! $("input[name='writer']").val()){
					alert(writererror);
					$("input[name='writer']").focus();
					return false;
				} else if(! $("input[name='subject']").val()){
					alert(subjecterror);
					$("input[name='subject']").focus();
					return false;
				} else if(! $("textarea[name='content']").val()){
					alert(contenterror);
					$("input[name='content']").focus();
					return false;
				}else if(! $("input[name='passwd']").val()){
					alert(passwderror);
					$("input[name='passwd']").focus();
					return false;
				}
			}
		);
		$("form[name='passwdform']").on(
			"submit",
			function(event){
				if(! $("input[name='passwd']").val()){
					alert(passwderror);
					$("input[name='passwd']").focus();
					return false;
				}
			}
		)
		// 글수정
		$("form[name='modifyform']").on(
			"submit",
			function( event ) {
				if( ! $("input[name='subject']").val() ) {
					alert( subjecterror );
					$("input[name='subject']").focus();
					return false;
				} else if( ! $("textarea[name='content']").val() ) {
					alert( contenterror );
					$("textarea[name='content']").focus();
					return false;
				} else if( ! $("input[name='passwd']").val() ) {
					alert( passwderror );
					$("input[name='passwd']").focus();
					return false;
				}	
			}
		);
	}
	
);



//simple Ajax
var request = null;
function show(){
	if(window.ActiveXObject){
		//IE
		try{
			request = new ActiveXObject("Msxml.XMLHTTP");
		}catch(e){ /*e == 이셉션 예외*/
			request = new ActiveXObjext("Microsoft.XMLHPPT");
		}
	}else{
		//IE가 아닌 경우
		request = new XMLHttpRequest();
	}
	var params = "id="+$("input[name='id']").val()
								+"&passwd=" +$("input[name='passwd']").val();
	var csrf_token=$("[name=csrfmiddlewaretoken]").val();
	
	request.open("POST", "ajax", true);
			/* ( post or get , url (주소입력하는자리) ) */
	request.setRequestHeader( "content-type", "application/x-www-form-urlencoded" );
	request.setRequestHeader( "X_CSRFToken", csrf_token);
	request.onreadystatechange=showresult;
	/*준비상태가 바뀌면 onreadystatechange 이벤트가 생길때마다 showresult 호출을 해라*/
	//request.send(null);
	request.send(params);
}
function showresult(){
	var msg = ""
	if (request.readyState == 4){
		if(request.status == 200){
			msg = request.responseText;	
/*			var data = request.responseText;*/
		}else{
			msg+=request.status+"에러발생<br>"
		}
	}else{
		msg+request.readySate+"통신중<br>";
	}
	$("#result").html(msg);
}


// JQuery Ajax
$(document).ready(
	function(){
		$.ajaxSetup({
			headers:{"X-CSRFToken":$("input[name='csrfmiddlewaretoken']").val()}
		});
	
		$("input[value='전송']").on(
			"click",
			function(event){
				/*json 표기법으로 작성해야된다
				  json안에 json을 넣을수있다 
				  key 문자열(""생략가능 json만 생략가능) : "value "*/
				$.ajax(
					{
						type:"post",
						url:"ajaxtext",
						data:{
							id:$("input[name='id']").val(),
							passwd:$("input[name='passwd']").val(),
						},
						dataType:"text",
						success : function(data){
							$("#result").html(data);
							// 출력할때는 "# " 표기해야한다
						},
						error : function(error){
							$("#result").html(errer);	
						}
					}
				);
					
			}
		);
		
		$("input[value='목록']").on(
			"click",
			function( event ) {
				$.ajax(
					{
						type : "POST",
						url : "ajaxjson",
						dataType : "json",
						success : function( data ) {
							var msg = "";							
							for( var i=0; i<data.members.length; i++ ) {
								msg += "이름 : " + data.members[i].name + "<br>"
									+ "나이 : " + data.members[i].age + "<br>"
									+ "전화번호 : " + data.members[i].tel + "<br><br>";  
							}	
							$("#result").html( msg );	
						}, 
						error : function( error ) {
							$("#result").html( error );
						}						
					}					
				);
				
			}			
		);
		$("input[value='목록']").on(
			"click",
			function(event){
				$.ajax(
					{
						type : "POST",
						url:"ajaxxml",
						dataType:"xml",
						success:function(data){
							var msg = ""
							$(data).find("member").each(
								function(index, item){
									msg+="이름:"+$(this).find("name").text()+"<br>"
										+"나이:"+$(this).find("age").text()+"<br>"
										+"전화번호:"+$(this).find("tel").text()+"<br><br>";
										/*자바스크립트는 끝나는 부분에 세미 클론 입력해야한다*/
									
								}
							);
							/*jqery 반복문 사용할때 each 사용하면 됨*/
							/*데이터 여러게 찾을때 find 함수사용*/
							$("#result").html(msg);
						},
						error:function(error){
							$("#result").html(error);
						}
					}
				)
			}
		
		);
		
		$("input[value='보기']").on(
			"click",
			function( event ) {
				$.ajax(
					{
						type : "POST",
						url : "ajaxxmljson",
						dataType : "xml",
						success : function( data ) {
							var msg = "";
							var users = eval("("+$(data).find("users").text()+")")
							$.each(
								users.user,
								function(index, item){
									msg +="이름:"+item.name+"<br>"
										+"나이:"+item.age+"<br>"
										+"전화번호:"+item.tel+"<br><br>"
								}
							);
							/*$("#result").html(msg);*/
							
							var title = "<th>이름</th><th>나이</th><th>전화번호</th>";
							$("<tr></tr>").html(title).appendTo("#tb");
							$.each(
								users.user,
								function(index,item){
									var u = "<td align='center'>"+item.name+"</td>"
										  + "<td align='center'>"+item.age+"</td>"
										  + "<td align='center'>"+item.tel+"</td>"
										
									$("<td></td>").html(u).appendTo("#tb");
								}
							)
						},
						error : function( error ) {
							$("#result").html( error );
						}						
					}
				);	
			}			
		);
	}
);