/**
 * 
 */

$(function () {
   
   
  $("#locationKindD").on("change", function(){
      var location = "";
   
         var t = "http://openapi.seoul.go.kr:8088/4f4f44766365737035374170685766/xml/citydata/1/5/";
      location = $(this).children("option:selected").text();
      t = t + location;
      $("#chartImg").css("display", "none");
      $("#chartBox").css("display", "");
   
   
    $.ajax({
    type: "GET",
    url: t,
    data: {},
    success: function(response){
       $(response).find('LIVE_PPLTN_STTS').each(function(){
         let male = parseFloat($(this).find('MALE_PPLTN_RATE').text());
         let female = parseFloat($(this).find('FEMALE_PPLTN_RATE').text());
         let age10 = parseFloat($(this).find('PPLTN_RATE_10').text());
         let age20 = parseFloat($(this).find('PPLTN_RATE_20').text());
         let age30 = parseFloat($(this).find('PPLTN_RATE_30').text());
         let age40 = parseFloat($(this).find('PPLTN_RATE_40').text());
         let age50 = parseFloat($(this).find('PPLTN_RATE_50').text());
         let age60 = parseFloat($(this).find('PPLTN_RATE_60').text());
         let age70 = parseFloat($(this).find('PPLTN_RATE_70').text());

             let sumtest = ``;
             let sumtest1 = ``;
             
             if(sumtest1 != null){
               var chart1 = Highcharts.chart('container1', {
                      chart: {
                          plotBackgroundColor: null,
                          plotBorderWidth: null,
                          plotShadow: false,
                          type: 'pie'
                      },
                      title: {
                          text: '연령대별 인구 비율',
                          align: 'center'
                      },
                      tooltip: {
                          pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                      },
                      accessibility: {
                          point: {
                              valueSuffix: '%'
                          }
                      },
                      legend: {//범례
                        floating: true,//범례를 차트 영역 위로 띄울 시 true 지정.
                        align: 'right',//수평 정렬 지정
                             verticalAlign: 'top',//수직 정렬 지정.
                             symbolRadius:0,//범례 심볼 radius 지정
                             symbolWidth:10,
                             symbolHeight:10,
                             itemDistance:17,//범례 간 간격 지정.
                             itemStyle: {
                             color:'#444',
                             fontSize: '14px',
                             fontWeight:'400'
                           },
                           x: 0,//가로 위치 지정.
                           y: 0,//세로 위치 지정.
                      },
                      plotOptions: {
                          pie: {
                              allowPointSelect: true,
                              cursor: 'pointer',
                              dataLabels: {
                                  enabled: true,
                                  format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                              }
                          }
                      },
                      series: [{
                          name: 'Ages',
                          colorByPoint: true,
                          data: [{
                              name: '10대',
                              y: age10,
                              sliced: true,
                              selected: true
                          }, {
                              name: '20대',
                              y: age20
                          },  {
                              name: '30대',
                              y: age30
                          }, {
                              name: '40대',
                              y: age40
                          }, {
                              name: '50대',
                              y: age50
                          },  {
                              name: '60대',
                              y: age60
                          }, {
                              name: '70대 이상',
                              y: age70
                          }]
                      }]
               });
                
             }

             if(sumtest != null){
                 var chart2 = Highcharts.chart('container2', {
                         chart: {
                             plotBackgroundColor: null,
                             plotBorderWidth: null,
                             plotShadow: false,
                             type: 'pie'
                         },
                         title: {
                             text: '성별별 인구 비율',
                             align: 'center'
                         },
                         tooltip: {
                             pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                         },
                         accessibility: {
                             point: {
                                 valueSuffix: '%'
                             }
                         },
                         legend: {//범례
                           floating: true,//범례를 차트 영역 위로 띄울 시 true 지정.
                           align: 'right',//수평 정렬 지정
                                verticalAlign: 'top',//수직 정렬 지정.
                                symbolRadius:0,//범례 심볼 radius 지정
                                symbolWidth:10,
                                symbolHeight:10,
                                itemDistance:17,//범례 간 간격 지정.
                                itemStyle: {
                                color:'#444',
                                fontSize: '14px',
                                fontWeight:'400'
                              },
                              x: 0,//가로 위치 지정.
                              y: 0,//세로 위치 지정.
                         },
                         plotOptions: {
                             pie: {
                                 allowPointSelect: true,
                                 cursor: 'pointer',
                                 dataLabels: {
                                     enabled: true,
                                     format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                                 }
                             }
                         },
                         series: [{
                             name: 'Gender',
                             colorByPoint: true,
                             data: [{
                                 name: '남성',
                                 y: male,
                                 sliced: true,
                                 selected: true
                             }, {
                                 name: '여성',
                                 y: female
                             }]
                         }]
                     });
             }
          });
      },
      error:function(){
         alert('xml데이터를 읽어오기 실패')
      }
    });
    });
    
   $(document).ready(function(){
      $.ajax({
         type : "GET",
         url : "http://openapi.seoul.go.kr:8088/657a425575646f6e3932446663456a/xml/TbCorona19CountStatus/1/5/",
         dataType : "xml",
         success: function(response){
            xmlParsing(response);
            },
         error : function(){
            alert('데이터 불러오기 실패')
         }
      });
      
      function xmlParsing(data){
         var dateList = [];
         var covidList = [];
         $(data).find('row').each(function(index, item){
            //console.log(item)  //값나오는거 확인 됨.
            let date = $(this).find('S_DT').text().substr(0, 10);
               dateList.unshift(date);
            let covid = parseInt($(this).find('SN_HJ').text());
               covidList.unshift(covid);
            //console.log(date, covid)  //값나오는거 확인 됨.
         });
         //console.log(dateList)
         //console.log(covidList)
         
         let sumtest3 = '';
         if(sumtest3 != null){
            var chart3 = Highcharts.chart('container3', {
                chart: {
                    type: 'line'
                },
                title: {
                    text: '최근 5일간 서울시 코로나 확진자 현황'
                },
                
                xAxis: {
                    categories: [dateList[0], dateList[1], dateList[2], dateList[3], dateList[4]]
                },
                yAxis: {
                    title: {
                        text: '확진자 수'
                    },
                    enabled: true
                },
                plotOptions: {
                    line: {
                        dataLabels: {
                            enabled: true
                        },
                        enableMouseTracking: false
                    }
                },
                series: [{
                    name: '확진자 현황',
                    data: [covidList[0], covidList[1], covidList[2], covidList[3], covidList[4]]
                }]
            });
               
         }
      }
   });
   
   $("#locationDay").on("change", function(){
		var locationk = $("#locationKindD2").children("option:selected").text();
		var day = $(this).children("option:selected").val();
		var csrf_token = $("input[name='csrfmiddlewaretoken']").val();
        day = parseInt(day)
		$("#chartImg2").css("display", "none");
		$("#popChart").css("display", "");
    	$.ajax({
			type:"POST",
			url:'main',
			dataType: "json",
			data:{'locationk':locationk, 'day':day, "csrfmiddlewaretoken" : csrf_token},
			success: function(data){
				Highcharts.chart('container4', {
				    chart: {
				        type: 'column'
				    },
				    title: {
				        text: ''
				    },
				    xAxis: {
				        categories: [
				            '1시',
				            '2시',
				            '3시',
				            '4시',
				            '5시',
				            '6시',
				            '7시',
				            '8시',
				            '9시',
				            '10시',
				            '11시',
				            '12시',
				            '13시',
				            '14시',
				            '15시',
				            '16시',
				            '17시',
				            '18시',
				            '19시',
				            '20시',
				            '21시',
				            '22시',
				            '23시',
				            '24시'
				        ],
				        crosshair: true
				    },
				    yAxis: {
				        min: 0,
				        title: {
				            text: '인구수'
				        },
		                labels: {
		                    enabled: true,
		                    formatter: function() {
		                    	return parseInt(this.value );
		                    }
		                }
				    },
				    tooltip: {
				        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
				        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
				            '<td style="padding:0"><b>{point.y:,.0f} 명</b></td></tr>',
				        footerFormat: '</table>',
				        shared: true,
				        useHTML: true
				    },
				    plotOptions: {
				        column: {
				            pointPadding: 0.2,
				            borderWidth: 0
				        }
				    },
				    series: [{
				        name: data.locationk,
				        data: [data.pred_sum[1], data.pred_sum[2], data.pred_sum[3], data.pred_sum[4], data.pred_sum[5],  
				        	   data.pred_sum[6], data.pred_sum[7], data.pred_sum[8], data.pred_sum[9], data.pred_sum[10],
				        	   data.pred_sum[11], data.pred_sum[12], data.pred_sum[13], data.pred_sum[14], data.pred_sum[15],
				        	   data.pred_sum[16], data.pred_sum[17], data.pred_sum[18], data.pred_sum[19], data.pred_sum[20],
				        	   data.pred_sum[21], data.pred_sum[22], data.pred_sum[23], data.pred_sum[0]]
				
				    }]
				});
				
			},
			error : function(request,error){
	            alert("code:"+request.status+"\n"+"error:"+error);
			}
		});

    });
   
   
   
});
   