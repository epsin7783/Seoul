/*회원가입*/

var iderror = "아이디를 입력하세요.";
var passwderror = "비밀번호를 입력하세요.";
var repasswderror = "비밀번호가 다릅니다.";
var nameerror = "이름을 입력하세요.";
var emailerror = "이메일을 입력하세요.";
var confirmerror = "아이디 중복확인을 해주세요";

/*function maincheck(){
	if(!mainform.id.value){
		alert(iderror);
		mainform.id.focus();
		return false;
	}else if(!mainform.passwd.value){
		alert(passwderror);
		mainform.passwd.focus();
		return false;
	}
}*/

$(document).ready(function(){
	$("form[name='mainform']").on("submit", function(event){
		if(!$("input[name='id']").val()){
			alert(iderror);
			$("input[name='id']").focus();
			return false;
		}else if(!$("input[name='pw']").val()){
			alert(passwderror);
			$("input[name='pw']").focus();
			return false;
		}
	});
	
	
	//회원가입
	$("form[name='inputform']").on("submit", function(event){
		if(!$("input[name='id']").val()){
			alert(iderror);
			$("input[name='id']").focus();
			return false;
		}else if(!$("input[name='name']").val()){
			alert("이름을 입력해 주세요");
			$("input[name='name']").focus();
			return false;
		}else if(!$("input[name='nickname']").val()){
			alert("닉네임을 입력해 주세요");
			$("input[name='nickname']").focus();
			return false;
		}else if(!$("input[name='pw']").val()){
			alert(passwderror);
			$("input[name='pw']").focus();
			return false;
		}else if($("input[name='pw']").val() != $("input[name='repw']").val()){
			alert(repasswderror);
			$("input[name='repw']").focus();
			return false;
		}else if(!$("input[name='name']").val()){
			alert(nameerror);
			$("input[name='name']").focus();
			return false;
		}else if(!$("input[name='email']").val()){
			alert(emailerror);
			$("input[name='email']").focus();
			return false;
		}else if(!$("input[name='phone1']").val()){
			alert("휴대폰번호를 정확히 입력해 주세요");
			$("input[name='phone1']").focus();
			return false;
		}else if(!$("input[name='phone2']").val()){
			alert("휴대폰번호를 정확히 입력해 주세요");
			$("input[name='phone2']").focus();
			return false;
		}else if(!$("input[name='phone3']").val()){
			alert("휴대폰번호를 정확히 입력해 주세요");
			$("input[name='phone3']").focus();
			return false;
		}
		
		/*if($("input[name='confirm']").val() == "0"){
			alert(confirmerror);
			$("input[name='id']").focus();
			return false;
		}*/
	});
	
	$("form[name='modifyform']").on("submit", function(event){
		if($("input[name='pw']").val() != $("input[name='repw']").val()){
			alert(repasswderror);
			$("input[name='pw']").focus();
			return false;
		}
	});
	
	//중복확인
	/*$("input[value='중복확인']").click(function(){
		var id = $("input[name='id']").val();
		if(!id){
			alert(iderror);
			$("input[name='id']").focus();
		}else{
			url = "confirm?id=" + id;
			window.open(url, "confirm", "toolbar=no, menubar=no, scrollbar=no, status=no, width=500, height=300, left=300, top=300");
		}
	});*/
	
	
	//아이디 중복확인 jquery
	/*$("td input[value='확인']").click(function(){
		var id = $("span").text();
		$("input[name='id']", opener.document.inputform).val(id); //opener(부모창)
		$("input[name='confirm']", opener.document.inputform).val("1"); //중복확인 체크
		self.close();
	});*/


	$("form[name='confirmform']").on("submit", function(){
		if(!$("input[name='id']").val()){
			alert(iderror);
			$("input[name='id']").focus();
			return false;
		}
	});
	
	
	//회원탈퇴
	$("form[name='passwdform']").on("submit", function(){
		if(!$("td input[name='pw']").val()){
			alert(passwderror);
			$("input[name='pw']").focus();
			return false;
		}
	});
	
	//ajaxSetup 장고토큰 설정
	$.ajaxSetup({
		headers: {"X-CSRFToken" : $("input[name='csrfmiddlewaretoken']").val()}
	});
	
	//아이디중복 ajax
	$("input[name='id']").keyup(function(){
		
		var id = $("input[name='id']").val();
		$.ajax({
			type : "POST",
			url : "idchk",
			data : { "id" : id },
			success : function(data){
				//alert("OK");
				$("#chk").html("아이디가 있습니다");
			},
			error : function(error){
				//$("#chk").html(error);
				//$("#chk").html("아이디가 없습니다");
				$("#chk").html("");
			}
		});
		
	});
	
	//닉네임중복 ajax
	$("input[name='nickname']").keyup(function(){
		
		var nickname = $("input[name='nickname']").val();
		$.ajax({
			type : "POST",
			url : "nicknamechk",
			data : { "nickname" : nickname },
			success : function(data){
				//alert("OK");
				$("#nicknamechk").html("닉네임이 있습니다");
			},
			error : function(error){
				//$("#chk").html(error);
				//$("#chk").html("아이디가 없습니다");
				$("#nicknamechk").html("");
			}
		});
		
	});
	
	/*$("input[name='pw']").keyup(function(){
		var pwlen = $("input[name='pw']").length; 
		if(pwlen < 4){
			$("#pwchk").html(pwlen);
		}else{
			$("#pwchk").html("");
		}
	});*/
	
	
});

//비밀번호 4자리이상
function pwchk(){
	var pwlen = $("input[name='pw']").val().length; 
	if(pwlen < 4){
		$("#pwchk").html("비밀번호는 4자리 이상입니다");
	}else{
		$("#pwchk").html("");
	}
}

//비밀번호 확인
function repwchk(){
	//var pw = $("input[name'passwd']").val();
	var pw = $("input[name='pw']").val();
	var repw = $("input[name='repw']").val();
	if(pw != repw){
		$("#repwchk").html("비밀번호가 다릅니다");
	}else{
		$("#repwchk").html("");
	}
}

//이메일 유효성검사
function emailchk(){
	var email = $("input[name='email']").val();
	var exptext = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/;
	if(exptext.test(email)==false){
	//이메일 형식이 알파벳+숫자@알파벳+숫자.알파벳+숫자 형식이 아닐경우			
		$("#emailchk").html("이메일이 유효하지 않습니다");
		userinput.email.focus();
		return false;
	}else{
		$("#emailchk").html("");
	}
}

//아이디 중복확인 javascript
/*function setid(id){
	opener.document.inputform.id.value = id;
	self.close();
}*/

$("#like").html("rrrr");


