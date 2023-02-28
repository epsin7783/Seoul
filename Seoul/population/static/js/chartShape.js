/**
 * 
 */

$(function () {
	$("#locationKindD").on("change", function(){
		let location = "";
		let t = "http://openapi.seoul.go.kr:8088/4f4f44766365737035374170685766/xml/citydata/1/5/";
		location = $(this).children("option:selected").text();
		t = t + location;
		
	
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
             
             /*if(sumtest1 != null){*/
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
                
             /*}*/

             /*if(sumtest != null){*/
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
             /*}*/
          });
      },
      error:function(){
         alert('xml데이터를 읽어오기 실패')
      }
 	});
    
   });
});
