#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-emmeans
Version  : 1.5.3
Release  : 43
URL      : https://cran.r-project.org/src/contrib/emmeans_1.5.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/emmeans_1.5.3.tar.gz
Summary  : Estimated Marginal Means, aka Least-Squares Means
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-car
Requires: R-estimability
Requires: R-lme4
Requires: R-mvtnorm
Requires: R-numDeriv
Requires: R-plyr
Requires: R-xtable
BuildRequires : R-car
BuildRequires : R-estimability
BuildRequires : R-lme4
BuildRequires : R-mvtnorm
BuildRequires : R-numDeriv
BuildRequires : R-plyr
BuildRequires : R-xtable
BuildRequires : buildreq-R

%description
linear, and mixed models. Compute contrasts or linear functions of EMMs,
  trends, and comparisons of slopes. Plots and other displays.
  Least-squares means are discussed, and the term "estimated marginal means"
  is suggested, in Searle, Speed, and Milliken (1980) Population marginal means

%prep
%setup -q -c -n emmeans
cd %{_builddir}/emmeans

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607542315

%install
export SOURCE_DATE_EPOCH=1607542315
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library emmeans
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library emmeans
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library emmeans
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc emmeans || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/emmeans/DESCRIPTION
/usr/lib64/R/library/emmeans/INDEX
/usr/lib64/R/library/emmeans/Meta/Rd.rds
/usr/lib64/R/library/emmeans/Meta/data.rds
/usr/lib64/R/library/emmeans/Meta/features.rds
/usr/lib64/R/library/emmeans/Meta/hsearch.rds
/usr/lib64/R/library/emmeans/Meta/links.rds
/usr/lib64/R/library/emmeans/Meta/nsInfo.rds
/usr/lib64/R/library/emmeans/Meta/package.rds
/usr/lib64/R/library/emmeans/Meta/vignette.rds
/usr/lib64/R/library/emmeans/NAMESPACE
/usr/lib64/R/library/emmeans/NEWS.md
/usr/lib64/R/library/emmeans/R/emmeans
/usr/lib64/R/library/emmeans/R/emmeans.rdb
/usr/lib64/R/library/emmeans/R/emmeans.rdx
/usr/lib64/R/library/emmeans/css/clean-simple.css
/usr/lib64/R/library/emmeans/data/Rdata.rdb
/usr/lib64/R/library/emmeans/data/Rdata.rds
/usr/lib64/R/library/emmeans/data/Rdata.rdx
/usr/lib64/R/library/emmeans/doc/FAQs.R
/usr/lib64/R/library/emmeans/doc/FAQs.Rmd
/usr/lib64/R/library/emmeans/doc/FAQs.html
/usr/lib64/R/library/emmeans/doc/basics.R
/usr/lib64/R/library/emmeans/doc/basics.Rmd
/usr/lib64/R/library/emmeans/doc/basics.html
/usr/lib64/R/library/emmeans/doc/comparisons.R
/usr/lib64/R/library/emmeans/doc/comparisons.Rmd
/usr/lib64/R/library/emmeans/doc/comparisons.html
/usr/lib64/R/library/emmeans/doc/confidence-intervals.R
/usr/lib64/R/library/emmeans/doc/confidence-intervals.Rmd
/usr/lib64/R/library/emmeans/doc/confidence-intervals.html
/usr/lib64/R/library/emmeans/doc/index.html
/usr/lib64/R/library/emmeans/doc/interactions.R
/usr/lib64/R/library/emmeans/doc/interactions.Rmd
/usr/lib64/R/library/emmeans/doc/interactions.html
/usr/lib64/R/library/emmeans/doc/messy-data.R
/usr/lib64/R/library/emmeans/doc/messy-data.Rmd
/usr/lib64/R/library/emmeans/doc/messy-data.html
/usr/lib64/R/library/emmeans/doc/models.Rmd
/usr/lib64/R/library/emmeans/doc/models.html
/usr/lib64/R/library/emmeans/doc/predictions.R
/usr/lib64/R/library/emmeans/doc/predictions.Rmd
/usr/lib64/R/library/emmeans/doc/predictions.html
/usr/lib64/R/library/emmeans/doc/sophisticated.R
/usr/lib64/R/library/emmeans/doc/sophisticated.Rmd
/usr/lib64/R/library/emmeans/doc/sophisticated.html
/usr/lib64/R/library/emmeans/doc/transformations.R
/usr/lib64/R/library/emmeans/doc/transformations.Rmd
/usr/lib64/R/library/emmeans/doc/transformations.html
/usr/lib64/R/library/emmeans/doc/utilities.R
/usr/lib64/R/library/emmeans/doc/utilities.Rmd
/usr/lib64/R/library/emmeans/doc/utilities.html
/usr/lib64/R/library/emmeans/doc/vignette-topics.Rmd
/usr/lib64/R/library/emmeans/doc/vignette-topics.html
/usr/lib64/R/library/emmeans/doc/xplanations.R
/usr/lib64/R/library/emmeans/doc/xplanations.Rmd
/usr/lib64/R/library/emmeans/doc/xplanations.html
/usr/lib64/R/library/emmeans/doc/xtending.R
/usr/lib64/R/library/emmeans/doc/xtending.Rmd
/usr/lib64/R/library/emmeans/doc/xtending.html
/usr/lib64/R/library/emmeans/extdata/cbpplist
/usr/lib64/R/library/emmeans/extdata/cbpppriorrglist
/usr/lib64/R/library/emmeans/extdata/cbpprglist
/usr/lib64/R/library/emmeans/extdata/cbppsigma
/usr/lib64/R/library/emmeans/help/AnIndex
/usr/lib64/R/library/emmeans/help/aliases.rds
/usr/lib64/R/library/emmeans/help/emmeans.rdb
/usr/lib64/R/library/emmeans/help/emmeans.rdx
/usr/lib64/R/library/emmeans/help/paths.rds
/usr/lib64/R/library/emmeans/html/00Index.html
/usr/lib64/R/library/emmeans/html/R.css
/usr/lib64/R/library/emmeans/tests/testthat.R
/usr/lib64/R/library/emmeans/tests/testthat/test-contrast.R
/usr/lib64/R/library/emmeans/tests/testthat/test-emmeans.R
/usr/lib64/R/library/emmeans/tests/testthat/test-emtrends.R
/usr/lib64/R/library/emmeans/tests/testthat/test-nested.R
/usr/lib64/R/library/emmeans/tests/testthat/test-ref_grid.R
