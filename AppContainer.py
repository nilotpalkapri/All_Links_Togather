import streamlit as st


st.markdown("""<h1 align="center" style="color:DarkBlue;">
            All Future Applications Link will be Available Here</h1>""", 
            unsafe_allow_html=True)
st.sidebar.markdown("""<h1 align="center" style="color:DarkBlue;">
                    All Future Applications Link will be Available Here</h1>""", 
                    unsafe_allow_html=True)
for i in range(2):
    st.markdown(' ')
    st.sidebar.markdown(' ')
#############################################################################################################
st.markdown("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<center><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.container {
  position: relative;
  width: 100%;
  max-width: 700px;
}
.container img {
  width: 100%;
  height: None;
}
.container .btn-one {
	color: #FFF;
	transition: all 0.3s;
	position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    font-size: 30px;
    cursor: pointer;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 5px #FFF;
    width: 80%;
}
.container .btn-one span {
	transition: all 0.3s;
}
.container .btn-one::before {
	content: '';
	position: absolute;
	bottom: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	opacity: 0;
	transition: all 0.3s;
	border-top-width: 3px;
	border-bottom-width: 3px;
	border-top-style: solid;
	border-bottom-style: solid;
	border-top-color: rgba(255,255,255,0.9);
	border-bottom-color: rgba(255,255,255,0.9);
	transform: scale(0.1, 1);
}
.container .btn-one:hover span {
	letter-spacing: 2px;
}
.container .btn-one:hover::before {
	opacity: 1;	
	transform: scale(1, 1);	
}
.container .btn-one::after {
	content: '';
	position: absolute;
	bottom: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	transition: all 0.3s;
	background-color: rgba(255,255,255,0.1);
}
.container .btn-one:hover::after {
	opacity: 0;	
	transform: scale(0.1, 1);
}
.container .btn-two {
	color: #FFF;
	transition: all 0.5s;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    font-size: 30px;
    padding: 16px 30px;
    cursor: pointer;
    text-align: center;
    box-shadow: 0 5px #FFF;
    width: 80%;
}
.container .btn-two span {
	z-index: 2;	
	display: block;
	position: absolute;
	width: 100%;
	height: 100%;	
}
.container .btn-two::before {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	transition: all 0.5s;
	border: 3px solid rgba(255,255,255,0.4);
	background-color: rgba(255,255,255,0.05);
}
.container .btn-two::after {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	transition: all 0.5s;
	border: 3px solid rgba(255,255,255,0.4);
	background-color: rgba(255,255,255,0.05);
}
.container .btn-two:hover::before {
  transform: rotate(-45deg);
  background-color: rgba(255,255,255,0);
}
.container .btn-two:hover::after {
  transform: rotate(45deg);
  background-color: rgba(255,255,255,0);
}
.container .btn-three {
	color: #FFF;
	transition: all 0.5s;
	position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    font-size: 30px;
    padding: 16px 30px;
    cursor: pointer;
    text-align: center;
    box-shadow: 0 5px #FFF;
    width: 80%;
}
.container .btn-three::before {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	background-color: rgba(255,255,255,0.1);
	transition: all 0.3s;
}
.container .btn-three:hover::before {
	opacity: 1 ;
	transform: scale(0.5,0.5);
}
.btn-three::after {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	opacity: 0;
	transition: all 0.3s;
	border: 3px solid rgba(255,255,255,0.5);
	transform: scale(1.2,1.2);
}
.container .btn-three:hover::after {
	opacity: 1;
	transform: scale(1,1);
}
.container .btn-four {
    border: 0 solid;
    box-shadow: inset 0 0 20px rgba(255, 255, 255, 0);
    outline: 1px solid;
    outline-color: rgba(255, 255, 255, .5);
    outline-offset: 0px;
    text-shadow: none;
    transition: all 1250ms cubic-bezier(0.19, 1, 0.22, 1);
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    font-size: 30px;
    padding: 16px 30px;
    cursor: pointer;
    text-align: center;
    box-shadow: 0 5px #111;
    width: 80%;
} 
.container .btn-four:hover {
  border: 1px solid;
  box-shadow: inset 0 0 20px rgba(255, 255, 255, .5), 0 0 20px rgba(255, 255, 255, .2);
  outline-color: rgba(255, 255, 255, 0);
  outline-offset: 15px;
  text-shadow: 1px 1px 2px #427388; 
}
</style>
</head>
<body><center>
<div class="container">
  <a href="https://crop-production-india-nil.herokuapp.com/" target="_blank">
  <img src="https://raw.githubusercontent.com/nilotpalkapri/All_Links_Togather/master/Decorator/crop_front.jpg" alt="" style="">
  <button class="btn btn-one"><h2 style="color: #ffffb5 ;"><b>Crop Production Data Analysis and Trends Visualization of India</b></h2></button>
  </a>
</div>
<div class="container">
  <a href="https://mushroom-classification-nil.herokuapp.com/" target="_blank">
  <img src="https://raw.githubusercontent.com/nilotpalkapri/All_Links_Togather/master/Decorator/mushroom_front.jpeg" alt="" style="">
  <button class="btn btn-four"><h2 style="color: #fdb5ff ;"><b>Mushroom Classification Web App</b></h2></button>
  </a>
</div>
 </center>     
</body>
</html>
""", unsafe_allow_html=True)


###########################################################################################################
st.sidebar.markdown("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<center><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.container {
  position: relative;
  width: 100%;
  max-width: 700px;
}
.container img {
  width: 100%;
  height: None;
}
.container .btn-one {
	color: #FFF;
	transition: all 0.3s;
	position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    font-size: 30px;
    cursor: pointer;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 5px #FFF;
    width: 80%;
}
.container .btn-one span {
	transition: all 0.3s;
}
.container .btn-one::before {
	content: '';
	position: absolute;
	bottom: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	opacity: 0;
	transition: all 0.3s;
	border-top-width: 3px;
	border-bottom-width: 3px;
	border-top-style: solid;
	border-bottom-style: solid;
	border-top-color: rgba(255,255,255,0.9);
	border-bottom-color: rgba(255,255,255,0.9);
	transform: scale(0.1, 1);
}
.container .btn-one:hover span {
	letter-spacing: 2px;
}
.container .btn-one:hover::before {
	opacity: 1;	
	transform: scale(1, 1);	
}
.container .btn-one::after {
	content: '';
	position: absolute;
	bottom: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	transition: all 0.3s;
	background-color: rgba(255,255,255,0.1);
}
.container .btn-one:hover::after {
	opacity: 0;	
	transform: scale(0.1, 1);
}
.container .btn-two {
	color: #FFF;
	transition: all 0.5s;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    font-size: 30px;
    padding: 16px 30px;
    cursor: pointer;
    text-align: center;
    box-shadow: 0 5px #FFF;
    width: 80%;
}
.container .btn-two span {
	z-index: 2;	
	display: block;
	position: absolute;
	width: 100%;
	height: 100%;	
}
.container .btn-two::before {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	transition: all 0.5s;
	border: 3px solid rgba(255,255,255,0.4);
	background-color: rgba(255,255,255,0.05);
}
.container .btn-two::after {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	transition: all 0.5s;
	border: 3px solid rgba(255,255,255,0.4);
	background-color: rgba(255,255,255,0.05);
}
.container .btn-two:hover::before {
  transform: rotate(-45deg);
  background-color: rgba(255,255,255,0);
}
.container .btn-two:hover::after {
  transform: rotate(45deg);
  background-color: rgba(255,255,255,0);
}
.container .btn-three {
	color: #FFF;
	transition: all 0.5s;
	position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    font-size: 30px;
    padding: 16px 30px;
    cursor: pointer;
    text-align: center;
    box-shadow: 0 5px #FFF;
    width: 80%;
}
.container .btn-three::before {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	background-color: rgba(255,255,255,0.1);
	transition: all 0.3s;
}
.container .btn-three:hover::before {
	opacity: 1 ;
	transform: scale(0.5,0.5);
}
.btn-three::after {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	opacity: 0;
	transition: all 0.3s;
	border: 3px solid rgba(255,255,255,0.5);
	transform: scale(1.2,1.2);
}
.container .btn-three:hover::after {
	opacity: 1;
	transform: scale(1,1);
}
.container .btn-four {
    border: 0 solid;
    box-shadow: inset 0 0 20px rgba(255, 255, 255, 0);
    outline: 1px solid;
    outline-color: rgba(255, 255, 255, .5);
    outline-offset: 0px;
    text-shadow: none;
    transition: all 1250ms cubic-bezier(0.19, 1, 0.22, 1);
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    font-size: 30px;
    padding: 16px 30px;
    cursor: pointer;
    text-align: center;
    box-shadow: 0 5px #111;
    width: 80%;
} 
.container .btn-four:hover {
  border: 1px solid;
  box-shadow: inset 0 0 20px rgba(255, 255, 255, .5), 0 0 20px rgba(255, 255, 255, .2);
  outline-color: rgba(255, 255, 255, 0);
  outline-offset: 15px;
  text-shadow: 1px 1px 2px #427388; 
}
</style>
</head>
<body><center>
<div class="container">
  <a href="https://crop-production-india-nil.herokuapp.com/" target="_blank">
  <img src="https://raw.githubusercontent.com/nilotpalkapri/All_Links_Togather/master/Decorator/crop_front.jpg" alt="" style="">
  <button class="btn btn-one"><h2 style="color: #ffffb5 ;"><b>Crop Production Data Analysis and Trends Visualization of India</b></h2></button>
  </a>
</div>
<div class="container">
  <a href="https://mushroom-classification-nil.herokuapp.com/" target="_blank">
  <img src="https://raw.githubusercontent.com/nilotpalkapri/All_Links_Togather/master/Decorator/mushroom_front.jpeg" alt="" style="">
  <button class="btn btn-four"><h2 style="color: #fdb5ff ;"><b>Mushroom Classification Web App</b></h2></button>
  </a>
</div>
 </center>     
</body>
</html>
""", unsafe_allow_html=True)
####################################################################################################
















###################################################################################################################
for i in range(10):
    st.write(' ')
st.markdown("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<center><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.fa {
  width: 15px;
  height: 15px;
  display: inline-block;
  padding: 20px;
  font-size: 20px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;  
  border: none;
  border-radius: 50%
}
</style>
</head>
<body><center>
<!--<h2>Style Social Media Buttons</h2>-->
<!--
<a href="https://wa.me/+918159853451" target="_blank">
  <img src="https://cdn0.iconfinder.com/data/icons/tuts/256/whatsapp.png" 
  alt="Whatsapp" style="width:25px;height:25px;border:0">
</a> -->
<a href="https://www.facebook.com/nilu.kapri/" target="_blank">
  <img src="https://cdn4.iconfinder.com/data/icons/free-social-media-icons/512/Facebook.png" 
  alt="Facebook" style="width:44px;height:44px;border:0">
</a>
<a href="https://instagram.com/Nilotpal__Kapri" target="_blank">
  <img src="https://cdn4.iconfinder.com/data/icons/social-media-2146/512/25_social-256.png" 
  alt="Instagram" style="width:44px;height:44px;border:0">
</a> 
<a href="https://m.me/106286494269703" target="_blank">
  <img src="https://cdn3.iconfinder.com/data/icons/social-media-2068/64/_Facebook_Messenger-512.png" 
  alt="Messenger" style="width:44px;height:44px;border:0">
</a>
<a href="https://twitter.com/nilotpalkapri" target="_blank">
  <img src="https://cdn3.iconfinder.com/data/icons/social-media-2068/64/_Twitter-256.png" 
  alt="Twitter" style="width:46px;height:46px;border:0">
</a>
<a href="https://www.youtube.com/channel/UCe_4uLTNbOvhJGHRVqqbHeQ" target="_blank">
  <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Youtube_colored_svg-512.png" 
  alt="YouTube" style="width:52px;height:54px;border:0">
</a>
<a href="mailto:nilotpal623401@gmail.com" target="_blank">
  <img src="https://cdn2.iconfinder.com/data/icons/once-again/48/Gmail.png" 
  alt="Mail" style="width:54px;height:54px;border:0">
</a>
<a href="https://www.linkedin.com/in/nilotpalkapri" target="_blank">
  <img src="https://cdn4.iconfinder.com/data/icons/free-social-media-icons/256/LinkedIn.png" 
  alt="Linkedin" style="width:44px;height:44px;border:0">
</a>
<a href="https://github.com/nilotpalkapri/" target="_blank">
  <img src="https://cdn4.iconfinder.com/data/icons/miu-hexagon-shadow-social/60/github-hexagon-shadow-social-media-256.png" 
  alt="Whatsapp" style="width:50px;height:50px;border:0">
</a>
<a href="https://independent.academia.edu/nilotpalkapri" target="_blank">
  <img src="https://image.flaticon.com/icons/png/512/25/25645.png" 
  alt="Academia" style="width:44px;height:44px;border:0">
</a>
<a href="https://orcid.org/0000-0001-7803-5957" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/ORCID_iD.svg/768px-ORCID_iD.svg.png" 
  alt="Orcid" style="width:46px;height:46px;border:0">
</a>
<a href="https://www.mendeley.com/profiles/nilotpal-kapri/" target="_blank">
  <img src="https://cdn.onlinewebfonts.com/svg/img_435968.png" 
  alt="Mendeley" style="width:52px;height:38px;border:0">
</a>
 </center>     
</body>
</html>
""", unsafe_allow_html=True)


################################################################################################
for i in range(10):
    st.sidebar.markdown(' ')
st.sidebar.markdown("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<center><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.fa {
  width: 15px;
  height: 15px;
  display: inline-block;
  padding: 20px;
  font-size: 20px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;  
  border: none;
  border-radius: 50%
}
</style>
</head>
<body><center>
<!--
<a href="https://wa.me/+918159853451" target="_blank">
  <img src="https://cdn0.iconfinder.com/data/icons/tuts/256/whatsapp.png" 
  alt="Whatsapp" style="width:25px;height:25px;border:0">
</a> -->
<a href="https://www.facebook.com/nilu.kapri/" target="_blank">
  <img src="https://cdn4.iconfinder.com/data/icons/free-social-media-icons/512/Facebook.png" 
  alt="Facebook" style="width:22px;height:22px;border:0">
</a>
<a href="https://instagram.com/Nilotpal__Kapri" target="_blank">
  <img src="https://cdn4.iconfinder.com/data/icons/social-media-2146/512/25_social-256.png" 
  alt="Instagram" style="width:22px;height:22px;border:0">
</a> 
<a href="https://m.me/106286494269703" target="_blank">
  <img src="https://cdn3.iconfinder.com/data/icons/social-media-2068/64/_Facebook_Messenger-512.png" 
  alt="Messenger" style="width:22px;height:22px;border:0">
</a>
<a href="https://twitter.com/nilotpalkapri" target="_blank">
  <img src="https://cdn3.iconfinder.com/data/icons/social-media-2068/64/_Twitter-256.png" 
  alt="Twitter" style="width:23px;height:23px;border:0">
</a>
<a href="https://www.youtube.com/channel/UCe_4uLTNbOvhJGHRVqqbHeQ" target="_blank">
  <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Youtube_colored_svg-512.png" 
  alt="YouTube" style="width:22px;height:25px;border:0">
</a>
<a href="mailto:nilotpal623401@gmail.com" target="_blank">
  <img src="https://cdn2.iconfinder.com/data/icons/once-again/48/Gmail.png" 
  alt="Mail" style="width:25px;height:25px;border:0">
</a>
<a href="https://www.linkedin.com/in/nilotpalkapri" target="_blank">
  <img src="https://cdn4.iconfinder.com/data/icons/free-social-media-icons/256/LinkedIn.png" 
  alt="Linkedin" style="width:22px;height:22px;border:0">
</a>
<a href="https://github.com/nilotpalkapri/" target="_blank">
  <img src="https://cdn4.iconfinder.com/data/icons/miu-hexagon-shadow-social/60/github-hexagon-shadow-social-media-256.png" 
  alt="Whatsapp" style="width:25px;height:25px;border:0">
</a>
<a href="https://independent.academia.edu/nilotpalkapri" target="_blank">
  <img src="https://image.flaticon.com/icons/png/512/25/25645.png" 
  alt="Academia" style="width:22px;height:22px;border:0">
</a>
<a href="https://orcid.org/0000-0001-7803-5957" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/ORCID_iD.svg/768px-ORCID_iD.svg.png" 
  alt="Orcid" style="width:23px;height:23px;border:0">
</a>
<a href="https://www.mendeley.com/profiles/nilotpal-kapri/" target="_blank">
  <img src="https://www.pinclipart.com/picdir/middle/568-5689345_2048-black-logo-mendeley-kecil-png-clipart.png" 
  alt="Mendeley" style="width:22px;height:21px;border:0">
</a>
 </center>     
</body>
</html>
""", unsafe_allow_html=True)


