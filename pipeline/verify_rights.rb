# -*- coding: utf-8 -*-
# RIGHTS.yaml 机器校验: 解析+分布+文件路径核对
require "yaml"
require "date"
d = YAML.safe_load(File.read("RIGHTS.yaml"), [Date])
books = d["books"]
puts "解析OK: #{books.size}本书"
puts "rights分布: #{books.values.group_by { |v| v["rights"] }.transform_values(&:size)}"
puts "scope分布: #{books.values.group_by { |v| v["scope"] }.transform_values(&:size)}"
p1 = books.select { |_, v| v["outreach_priority"] == 1 }.keys.sort
puts "P1名单(#{p1.size}): #{p1.join(", ")}"
pd = books.select { |_, v| v["pd_cn"] }.map { |k, v| [k, v["pd_cn"].year] }.sort_by { |_, y| y }
puts "公有倒计时: #{pd.map { |k, y| "#{k}=#{y}" }.join("  ")}"
missing = books.values.map { |v| v["file"] }.reject { |f| File.exist?(f) }
puts missing.empty? ? "文件路径核对: #{books.size}/#{books.size} 全部存在" : "缺失: #{missing}"
