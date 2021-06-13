#!/bin/zsh
#
#**********************************
#Author:	Raymond
#QQ:		
#Date:		2021-06-13
#Filename:	setup.zsh
#URL:		
#Description:	Set up of the dockerfiles of stroke prediction api
#**********************************

route=$(pwd)
# ls $route/docker-configuration/script
docker build -t stroke-base $route/docker-configuration/stroke-base/.
docker build -t stroke-flask $route/docker-configuration/stroke-flask/.
docker build -t stroke-streamlit $route/docker-configuration/stroke-streamlit/.