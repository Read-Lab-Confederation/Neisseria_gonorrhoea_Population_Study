
# Copyright (c) 2014 Matthew Ezewudo <mezewud@emory.edu>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.



tet_table <- read.table("~/desktop/noncore/Tet_Resis_table")
for (i in (1:nrow(tet_table))){
  result <-fisher.test(matrix(c(tet_table[i,2],tet_table[i,4],tet_table[i,3],tet_table[i,5]),2,2),alternative = "greater")
  tet_table$Fisher[i]<- result$p.value
}

tet_table_ordered <- tet_table[order(tet_table$Fisher),]
resulted <- fdrtool(tet_table_ordered$Fisher, statistic=c("pvalue"))

for (i in (1:nrow(tet_table_ordered))){
tet_table_ordered$fdr[i] <- resulted$qval[i]
}

Az_table <- read.table("~/desktop/noncore/Az_Resis_table")
for (i in (1:nrow(tet_table))){
  result <-fisher.test(matrix(c(Az_table[i,2],Az_table[i,4],Az_table[i,3],Az_table[i,5]),2,2),alternative = "greater")
  Az_table$Fisher[i]<- result$p.value
}
Az_table_ordered <- Az_table[order(Az_table$Fisher),]
resulted <- fdrtool(Az_table_ordered$Fisher, statistic=c("pvalue"))

for (i in (1:nrow(Az_table_ordered))){
  Az_table_ordered$fdr[i] <- resulted$qval[i]
}


Cf_table <- read.table("~/desktop/noncore/Cf_Resis_table")
for (i in (1:nrow(Cf_table))){
  result <-fisher.test(matrix(c(Cf_table[i,2],Cf_table[i,4],Cf_table[i,3],Cf_table[i,5]),2,2),alternative = "greater")
  Cf_table$Fisher[i]<- result$p.value
}
Cf_table_ordered <- Cf_table[order(Cf_table$Fisher),]
resulted <- fdrtool(Cf_table_ordered$Fisher, statistic=c("pvalue"))

for (i in (1:nrow(Cf_table_ordered))){
  Cf_table_ordered$fdr[i] <- resulted$qval[i]
}

write.table(Az_table_ordered, file="~/desktop/Az", row.names=FALSE, col.names=FALSE, sep="\t")
write.table(Cf_table_ordered, file="~/desktop/Cf", row.names=FALSE, col.names=FALSE, sep="\t")
write.table(tet_table_ordered, file="~/desktop/tet", row.names=FALSE, col.names=FALSE, sep="\t")
