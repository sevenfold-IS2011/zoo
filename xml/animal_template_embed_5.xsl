<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
			<xsl:for-each select="zoo:area">
			<xsl:if test="@id=5">
				<h2>Area <xsl:value-of select="./@nome"/>:</h2>
					<xsl:for-each select="zoo:animale">

					<div class="animale">
						<img class="animal">
      					<xsl:attribute name="src"><xsl:value-of select="zoo:img"/></xsl:attribute>
      			</img>
						<div class="testo">
							<h4>Scheda:</h4>
							<p>Nome: <xsl:value-of select="zoo:nome"/></p>
							<p>Età: <xsl:value-of select="zoo:eta"/></p>
							<p>Sesso: <xsl:value-of select="zoo:sesso"/></p>
						</div>
					</div>

					</xsl:for-each>
			</xsl:if>
			</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>

