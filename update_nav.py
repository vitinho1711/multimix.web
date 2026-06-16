import os
import glob
import re

nav_html = """<nav id="main-nav" class="fixed top-0 w-full z-50 bg-white/80 dark:bg-slate-950/80 backdrop-blur-xl border-b border-slate-200/50 dark:border-slate-800/50 shadow-sm">
<div class="flex justify-between items-center px-6 md:px-8 py-3 md:py-4 max-w-screen-2xl mx-auto border-none">
  <!-- Logo -->
  <a href="index.html" class="flex items-center shrink-0">
    <img src="logo.png" alt="MultMix Distribuidora" class="h-10 md:h-12 w-auto object-contain">
  </a>
  <!-- Desktop Nav -->
  <div class="hidden md:flex items-center gap-4 lg:gap-8 font-sans tracking-tight font-medium text-sm">
    <a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors relative group" href="index.html">Home<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-[#98d920] group-hover:w-full transition-all duration-300"></span></a>
    <a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors relative group" href="sobre.html">Sobre<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-[#98d920] group-hover:w-full transition-all duration-300"></span></a>
    <a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors relative group" href="categorias.html">Categorias<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-[#98d920] group-hover:w-full transition-all duration-300"></span></a>
    <a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors relative group" href="marcas_parceiras.html">Parceiros<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-[#98d920] group-hover:w-full transition-all duration-300"></span></a>
    <a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors relative group" href="logistica.html">Logística<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-[#98d920] group-hover:w-full transition-all duration-300"></span></a>
    <a class="text-slate-600 dark:text-slate-400 hover:text-slate-950 dark:hover:text-white transition-colors relative group" href="contato.html">Contato<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-[#98d920] group-hover:w-full transition-all duration-300"></span></a>
  </div>
  <div class="flex items-center gap-3 border-none">
    <a href="trabalhe_conosco.html" class="hidden md:inline-flex bg-tertiary-fixed text-on-tertiary-fixed px-5 py-2.5 text-sm font-bold rounded-sm hover:opacity-90 transition-all active:scale-[0.99] shrink-0">Trabalhe Conosco</a>
    <!-- Hamburger (mobile) -->
    <button id="menu-toggle" class="md:hidden flex flex-col gap-1.5 p-2 group border-none" aria-label="Menu">
      <span class="block w-6 h-0.5 bg-slate-800 dark:bg-white transition-all duration-300 group-[.open]:rotate-45 group-[.open]:translate-y-2"></span>
      <span class="block w-6 h-0.5 bg-slate-800 dark:bg-white transition-all duration-300 group-[.open]:opacity-0"></span>
      <span class="block w-6 h-0.5 bg-slate-800 dark:bg-white transition-all duration-300 group-[.open]:-rotate-45 group-[.open]:-translate-y-2"></span>
    </button>
  </div>
</div>
<!-- Mobile Menu -->
<div id="mobile-menu" class="md:hidden bg-white dark:bg-slate-950 border-t border-slate-100 dark:border-slate-800">
  <div class="px-6 py-4 flex flex-col gap-4 text-sm font-medium">
    <a class="text-slate-700 dark:text-slate-300 hover:text-[#98d920] transition-colors py-1" href="index.html">Home</a>
    <a class="text-slate-700 dark:text-slate-300 hover:text-[#98d920] transition-colors py-1" href="sobre.html">Sobre</a>
    <a class="text-slate-700 dark:text-slate-300 hover:text-[#98d920] transition-colors py-1" href="categorias.html">Categorias</a>
    <a class="text-slate-700 dark:text-slate-300 hover:text-[#98d920] transition-colors py-1" href="marcas_parceiras.html">Parceiros</a>
    <a class="text-slate-700 dark:text-slate-300 hover:text-[#98d920] transition-colors py-1" href="logistica.html">Logística</a>
    <a class="text-slate-700 dark:text-slate-300 hover:text-[#98d920] transition-colors py-1" href="contato.html">Contato</a>
    <a href="trabalhe_conosco.html" class="bg-tertiary-fixed text-on-tertiary-fixed px-5 py-2.5 text-sm font-bold text-center rounded-sm mt-2">Trabalhe Conosco</a>
  </div>
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
