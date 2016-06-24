#! /usr/bin/vim -S
"set expandtab
set shiftwidth=2
set tabstop=2

let g:test_all_test=['/bin/bash', '-c', "py.test"]
let g:test_current_ut=['py.test', '--color=yes']
let g:test_current_at=['py.test', '--color=yes']
