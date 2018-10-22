webpackJsonp([1],{NHnr:function(e,t,i){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=i("7+uW"),n=i("mtWM"),s=i.n(n),r={data:function(){return{options:[{text:"Text",value:"Text"},{text:"Number",value:"Number"},{text:"Date",value:"Date"},{text:"Enum",value:"Enum"}],things:[{text:"Option 1",value:1},{text:"Option 2",value:2},{text:"Option 3",value:3}],risks:[],errors:[],rows:[],risk_type:"",fieldz:[]}},methods:{addField:function(){document.createElement("tr"),this.rows.push({field_name_row:"",field_type_select_row:"",field_data:""})},removeElement:function(e){this.rows.splice(e,1)},fetchRisks:function(){var e=this;s.a.get("/api/risks/").then(function(t){e.risks=t.data}).catch(function(t){e.errors.push(t)})},postRisk:function(){var e=this;this.rows.forEach(function(t){e.fieldz.push({name:t.field_name_row,field_type:t.field_type_select_row}),console.log(t.field_name_row)}),s.a.post("/api/risks/",{risk_type:this.risk_type,fieldz:this.fieldz}).then(function(t){e.fetchRisks(),console.log(t)}).catch(function(t){e.errors.push(t)})}},created:function(){this.fetchRisks()}},o={render:function(){var e=this,t=e.$createElement,i=e._self._c||t;return i("div",{attrs:{id:"app"}},[i("div",{staticClass:"jumbotron"},[i("h1",{staticClass:"display-4"},[e._v("Risk Creator")]),e._v(" "),i("br"),i("br"),e._v(" "),i("h2",[e._v("Create a new risk type")]),e._v("\r\n    Risk Type:\r\n    "),i("input",{directives:[{name:"model",rawName:"v-model",value:e.risk_type,expression:"risk_type"}],attrs:{type:"text",placeholder:"Car Insurance"},domProps:{value:e.risk_type},on:{input:function(t){t.target.composing||(e.risk_type=t.target.value)}}})]),e._v(" "),i("div",{staticClass:"container"},[i("table",{directives:[{name:"show",rawName:"v-show",value:e.rows.length>0,expression:"rows.length > 0"}],staticClass:"table"},[e._m(0),e._v(" "),i("tbody",e._l(e.rows,function(t,a){return i("tr",{key:a},[i("td",[i("input",{directives:[{name:"model",rawName:"v-model",value:t.field_name_row,expression:"row.field_name_row"}],attrs:{type:"text"},domProps:{value:t.field_name_row},on:{input:function(i){i.target.composing||e.$set(t,"field_name_row",i.target.value)}}})]),e._v(" "),i("td",[i("select",{directives:[{name:"model",rawName:"v-model",value:t.field_type_select_row,expression:"row.field_type_select_row"}],on:{change:function(i){var a=Array.prototype.filter.call(i.target.options,function(e){return e.selected}).map(function(e){return"_value"in e?e._value:e.value});e.$set(t,"field_type_select_row",i.target.multiple?a:a[0])}}},e._l(e.options,function(t){return i("option",{key:t.id,domProps:{value:t.value}},[e._v("\r\n                    "+e._s(t.text)+"\r\n                  ")])}))]),e._v(" "),"Enum"===t.field_type_select_row?i("div",[i("td",[i("select",{directives:[{name:"model",rawName:"v-model",value:t.field_data,expression:"row.field_data"}],on:{change:function(i){var a=Array.prototype.filter.call(i.target.options,function(e){return e.selected}).map(function(e){return"_value"in e?e._value:e.value});e.$set(t,"field_data",i.target.multiple?a:a[0])}}},e._l(e.things,function(t){return i("option",{key:t.id,domProps:{value:t.value}},[e._v("\r\n                    "+e._s(t.text)+"\r\n                  ")])}))])]):"Text"===t.field_type_select_row?i("div",[i("td",[i("input",{directives:[{name:"model",rawName:"v-model",value:t.field_data,expression:"row.field_data"}],attrs:{type:"text"},domProps:{value:t.field_data},on:{input:function(i){i.target.composing||e.$set(t,"field_data",i.target.value)}}})])]):"Date"===t.field_type_select_row?i("div",[i("td",[i("input",{directives:[{name:"model",rawName:"v-model",value:t.field_data,expression:"row.field_data"}],attrs:{type:"date"},domProps:{value:t.field_data},on:{input:function(i){i.target.composing||e.$set(t,"field_data",i.target.value)}}})])]):i("div",[i("td",[i("input",{directives:[{name:"model",rawName:"v-model",value:t.field_data,expression:"row.field_data"}],attrs:{type:"text"},domProps:{value:t.field_data},on:{input:function(i){i.target.composing||e.$set(t,"field_data",i.target.value)}}})])]),e._v(" "),i("td",[i("button",{staticClass:"btn btn-danger",staticStyle:{cursor:"pointer"},on:{click:function(t){e.removeElement(a)}}},[e._v("Remove")])])])}))])]),e._v(" "),i("p"),e._v(" "),i("button",{staticClass:"button btn-primary",on:{click:e.addField}},[e._v("Add Field")]),e._v(" "),i("button",{staticClass:"button btn-success",on:{click:e.postRisk}},[e._v("Create Risk")]),e._v(" "),i("hr"),e._v(" "),i("h2",[e._v("Current Risks in Database")]),e._v(" "),i("div",{staticClass:"risk_list"},[e.risks&&0===e.risks.length?i("p",[e._v("No Risks")]):e._e(),e._v(" "),e._l(e.risks,function(t){return i("div",{key:t.id,staticClass:"risk"},[i("p",{staticClass:"risk-type"},[e._v("Risk Type: "),i("strong",[e._v(e._s(t.risk_type))]),e._v(", with Fields:")]),e._v(" "),t.fieldz&&t.fieldz.length?i("ul",e._l(t.fieldz,function(t){return i("li",{key:t.id},[i("u",[e._v(e._s(t.name))]),e._v(" of type: "),i("u",[e._v(e._s(t.field_type))])])})):e._e()])})],2),e._v(" "),i("hr")])},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("thead",[t("tr",[t("td",[t("strong",[this._v("Field Name")])]),this._v(" "),t("td",[t("strong",[this._v("Field Type")])]),this._v(" "),t("td",[t("strong",[this._v("Data")])])])])}]};var l=i("VU/8")(r,o,!1,function(e){i("ypce")},null,null).exports;i("qb6w");a.a.config.productionTip=!1,new a.a({el:"#app",components:{App:l},template:"<App/>"})},qb6w:function(e,t){},ypce:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.922378040c8616c01a70.js.map