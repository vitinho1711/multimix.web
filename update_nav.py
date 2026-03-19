import os
import glob
import re

nav_html = """<nav class="fixed top-0 w-full z-50 bg-white/80 dark:bg-slate-950/80 backdrop-blur-xl border-b border-slate-200/50 dark:border-slate-800/50 shadow-sm">
<div class="flex justify-between items-center px-8 py-4 max-w-screen-2xl mx-auto">
<div class="text-2xl font-black tracking-tighter text-slate-950 dark:text-white uppercase"><a href="index.html">MultMix</a></div>
<div class="hidden md:flex items-center gap-4 lg:gap-8 font-sans tracking-tight font-medium text-sm flex-wrap">
<a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors" href="index.html">Home</a>
<a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors" href="sobre.html">Sobre</a>
<a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors" href="categorias.html">Categorias</a>
<a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors" href="marcas_parceiras.html">Parceiros</a>
<a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors" href="logistica.html">Logística</a>
<a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors" href="blog.html">Blog</a>
<a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors" href="contato.html">Contato</a>
</div>
<a href="trabalhe_conosco.html" class="bg-tertiary-fixed text-on-tertiary-fixed px-6 py-2.5 text-sm font-bold rounded-sm hover:opacity-90 transition-all active:scale-[0.99] ml-4 shrink-0 overflow-hidden text-center">Trabalhe Conosco</a>
</div>
</nav>"""

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(r'<nav.*?</nav>', nav_html, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
        
print("Links de navegacao atualizados com sucesso em todas as paginas!")
