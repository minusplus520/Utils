
call plug#begin('~/.vim/plugged')
"Plug 'octol/vim-cpp-enhanced-highlight'
"Plug 'tomasiser/vim-code-dark'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
"Plug 'easymotion/vim-easymotion'    "quick jump  syntax \w \b \jklh \s
" Plug 'mg979/vim-visual-multi'
Plug 'scrooloose/nerdcommenter'  " auto add comment
"Plug 'Valloric/YouCompleteMe'
"Plug 'Yggdroot/indentLine'
"Plug 'junegunn/fzf.vim'
"Plug 'tpope/vim-surround'
"Plug 'mhinz/vim-signify'
"Plug 'ngemily/vim-vp4'
if v:version >= 704
   "Plug 'andymass/vim-matchup'
endif
""" plug in for lsp clangd
" Plug 'mattn/vim-lsp-settings'
" Plug 'prabirshrestha/async.vim'
" Plug 'prabirshrestha/vim-lsp'
" Plug 'prabirshrestha/asyncomplete.vim'
" Plug 'prabirshrestha/asyncomplete-lsp.vim'
""" pub for coc
Plug 'junegunn/fzf', {'dir': '~/.fzf','do': './install --all'}
Plug 'junegunn/fzf.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'antoinemadec/coc-fzf'
call plug#end()
"
" set rtp+=~/.vim/bundle/Vundle.vim
" call vundle#begin()
" Plugin 'VundleVim/Vundle.vim'
" Plugin 'Valloric/YouCompleteMe'
" call vundle#end()
"

set encoding=utf-8
syntax on
set nocompatible 
set wildmode=list:longest
setglobal complete-=i
 " set noshowmode

set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4

set hidden          "for buffer
set smarttab

set ruler        
set backspace=2   
"set ic           
set ru           
set ai
set hlsearch     
set incsearch    
set smartindent  
set confirm      
set history=100  

set isk-=:

set laststatus=2
set ttymouse=xterm2
set mouse=a
set list
set listchars=tab:>-
"set statusline=%4*%<\%m%<[%f\%r%h%w]\ [%{&ff},%{&fileencoding},%Y]%=\[Position=%l,%v,%p%%]

" conventional mapping
map X dWWP
map mm :marks<CR>
map <leader>w :w<CR>
map <leader>v :vnew<CR>
map <leader>n :new<CR>
map <leader>q :q<CR>
map <leader>Q :q!<CR>
map <leader>c :close<CR>
map <leader>s :set hls!<BAR>set hls?<CR>
map <leader>e :NERDTreeToggle<CR>
map <leader>f :FufFileWithCurrentBufferDir<CR>
map <leader>F :FufFile<CR>
map <leader>b :FufBuffer<CR>


map! <C-a> <ESC>0
map! <C-e> <ESC>A
map! <C-f> <Right>
map! <C-b> <Left>

map! <C-d> <ESC>lBdEi
map! <C-w> <ESC>lbdei 

nnoremap <F2> : /ZEBU_ROOT=<CR>
"nnoremap <F3> : /cluster_split<CR>
nnoremap ./ lbveyB/<C-R>"<CR>

"ctrl c
"vnoremap y "+y 
"vnoremap // y/<C-R>"<CR>
vnoremap <C-c> "+y


" mapping for tags
map tr :!rtags -R --vi .<CR>
map tc :!ctags *<CR>
map ]] g<C-]>
map <F3> g<C-]>
"map ]] g]
"map <F3> g]
nnoremap gr gT

" mapping for programming short cut
map ,b bi{<ESC>ea}<ESC>
map ,p bi(<ESC>ea)<ESC>
map! <C-o>l <ESC>la
map! <C-o>o ()<ESC>i
map! <C-o>k []<ESC>i
map! <C-o>v <><ESC>i
map! <C-o>u {}<ESC>i
map! <C-o>s ''<ESC>i
map! <C-o>d ""<ESC>i
" mapping for eruby
map! <C-o>i <ESC>a\|\|<ESC>i
map! <C-o>% <%  %><ESC>hhi
map! <C-o>5 <%=  %><ESC>hhi
" mapping for perl
map! <C-o>r ->
map! <C-o>m => 
map! <C-o>n ::
" mapping for html
map! <C-o>! <!--  --><ESC>3hi
map! <C-o>c /*  */<ESC>2hi

" mapping for tab
nmap t1 :tabfirst<CR>
nmap t0 :tablast<CR>
nmap tn :tabnew<CR>
nmap tj   :tabn<CR>
nmap tk   :tabp<CR>

nmap bn :bn<CR>
nmap bp :bp<CR>

" mapping for c-tags
inoremap /-- //-----------------------------------------------------------------------//


function IsBinary()
    if (&binary == 0)
        return ""
    else
        return "[Binary]"
    endif
endfunction

function FileSize()
    let bytes = getfsize(expand("%:p"))
    if bytes <= 0
        return "[Empty]"
    endif
    if bytes < 1024
        return "[" . bytes . "B]"
    elseif bytes < 1048576
        return "[" . (bytes / 1024) . "KB]"
    else
        return "[" . (bytes / 1048576) . "MB]"
    endif
endfunction

set statusline=%#filepath#[%{expand('%:p')}]%#filetype#[%{strlen(&fenc)?&fenc:&enc},\ %{&ff},\ %{strlen(&filetype)?&filetype:'plain'}]%#filesize#%{FileSize()}%{IsBinary()}%=%#position#%c,%l/%L\ [%3p%%]

hi filepath cterm=none ctermbg=238 ctermfg=40
hi filetype cterm=none ctermbg=238 ctermfg=45
hi filesize cterm=none ctermbg=238 ctermfg=225
hi position cterm=none ctermbg=238 ctermfg=228

"colorscheme solarized
"colorscheme minty
"colorscheme forgotten-dark

set t_Co=256
set background=dark
set cursorline
"set cursorcolumn
set smartcase
set ignorecase
set nowrap
set autowrite
set guifont=Monaco\ 12
set nu

"#execute pathogen#infect()
"#call pathogen#helptags() " generate helptags for everything in ‘runtimepath’
syntax on
filetype plugin indent on

"jump to last position
if has("autocmd")
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif

" <Ctrl-l> redraws the screen and removes any search highlighting.
nnoremap <silent> <CR> :nohl<CR><CR>

:set guioptions-=m  "remove menu bar
:set guioptions-=T  "remove toolbar
:set guioptions-=r  "remove right-hand scroll bar
:set guioptions-=L  "remove left-hand scroll bar

"set tag path
"set tags=./tags
set tags=./tags,./TAGS,tags;~,TAGS;~

"add cs database
"if $HOSTNAME !~ "berry"
"  cs add $CSCOPE_DBendif
"endif

" nerdcommenter
" Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1

" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1

" Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'

" Set a language to use its alternate delimiters by default
let g:NERDAltDelims_java = 1

" Add your own custom formats or override the defaults
let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }

" Allow commenting and inverting empty lines (useful when commenting a region)
let g:NERDCommentEmptyLines = 1

" Enable trimming of trailing whitespace when uncommenting
let g:NERDTrimTrailingWhitespace = 1




"*****************************************************************************************"
"  For Clangd
"*****************************************************************************************"
" autocmd FileType cpp  source ~/.vim/.vimrc_clangd
" let g:lsp_diagnostics_signs_priority_map = {
"           \'LspError': 12,
"           \'LspWarning': 12,
"           \'LspInformation': 11,
"           \'LspHint': 11,
"           \}
" "let g:lsp_semantic_enabled = 1
" nmap <F8> <Plug>(lsp-definition)
" nmap <F7> <Plug>(lsp-peek-definition)
" " nmap <F8> <Plug>(lsp-next-diagnostic)
" " nmap <F9> <Plug>(lsp-previous-diagnostic)
" nmap <F6> <Plug>(lsp-declaration)
" nmap <F5> <Plug>(lsp-peek-declaration)
" nmap <leader>d <Plug>(lsp-document-diagnostics)
" let g:lsp_diagnostics_float_cursor = 1

"*****************************************************************************************"
"  For nerd commenter
"*****************************************************************************************"
map // <plug>NERDCommenterToggle



"*****************************************************************************************"
"  For coc
"*****************************************************************************************"
" autocmd FileType cpp  source ~/.vim/.vimrc_clangd
source  ~/.vimrc_coc


"*****************************************************************************************"
"  For asyncomplete
"*****************************************************************************************"
" inoremap <expr> <Tab>   pumvisible() ? "\<C-n>" : "\<Tab>"
" inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
" inoremap <expr> <cr>    pumvisible() ? asyncomplete#close_popup() : "\<cr>"
" inoremap <c-space> <Plug>(asyncomplete_force_refresh)

"*****************************************************************************************"
" For airline
"*****************************************************************************************"
"for airline
"set status line"
set laststatus=2
"enable powerline-fonts"
" let g:airline_powerline_fonts = 1
" enable tabline"
let g:airline#extensions#tabline#enabled = 1
" show buffer number"
let g:airline#extensions#tabline#formatter = 'unique_tail'
let g:airline_theme='powerlineish'
" let g:airline_section_c = '%<%F%m %#__accent_red#%{airline#util#wrap(airline#parts#readonly(),0)}%#__restore__#'


