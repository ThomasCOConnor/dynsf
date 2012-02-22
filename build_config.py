
extra_compile_args = ['-fopenmp']
extra_link_args = ['-fopenmp']

# Let local_compiler be None in order to use the default compiler
#
local_compiler = None
local_linker = local_compiler


# # Example: Use icc instead of the default (gcc) compiler
# #
# local_compiler = 'icc'
# extra_compile_args = ['-openmp', '-xHOST', '-O3', '-fno-alias', '-fPIC']

# local_linker = local_compiler
# local_link_shared = ['-shared']
# extra_link_args = ['-openmp']
