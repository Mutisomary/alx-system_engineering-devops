#!/usr/bin/env ruby
# match a string starting with h, end with n and have a single middle character
puts ARGV[0].scan(/^h.n$/).join
