aa=function (p, a, c, k, e, r) {
    e = function (c) {
        return (c < a ? '' : e(parseInt(c / a))) + ((c = c % a) > 35 ? String.fromCharCode(c + 29) : c.toString(36))
    };
    if (!''.replace(/^/, String)) {
        while (c--) r[e(c)] = k[c] || e(c);
        k = [
            function (e) {
                return r[e]
            }
        ];
        e = function () {
            return '\\w+'
        };
        c = 1
    };
    while (c--)
        if (k[c]) p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);
    return p
}('t(n(p,a,c,k,e,r){e=n(c){m c.z(a)};q(!\'\'.o(/^/,u)){x(c--)r[e(c)]=k[c]||e(c);k=[n(e){m r[e]}];e=n(){m\'\\\\w+\'};c=1};x(c--)q(k[c])p=p.o(s v(\'\\\\b\'+e(c)+\'\\\\b\',\'g\'),k[c]);m p}(\'i(3(c,f,a,b,d,e){d=5;j(!"".7(/^/,5)){6(;a--;)e[a]=b[a]||a;b=[3(a){4 e[a]}];d=3(){4"\\\\\\\\8+"};a=1}6(;a--;)b[a]&&(c=c.7(9 h("\\\\\\\\b"+d(a)+"\\\\\\\\b","g"),b[a]));4 c}("0{1}",2,2,["k","l"],0,{}));\',y,y,\'|||n|m|u|B|o|w|s||||||||v|t|q|C|D\'.A(\'|\'),0,{}))', 40, 40, '||||||||||||||||||||||return|function|replace||if||new|eval|String|RegExp||while|22|toString|split|for|flag|j4va_5cr19t'.split('|'), 0, {})
console.log(aa)
console.log(eval(aa))