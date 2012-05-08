<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="/">
		<xsl:for-each select="zoo:animal">
			<p>Ciao, sono <xsl:value-of select="zoo:name"/>, </p>
			<p>sono un <xsl:value-of select="zoo:gender"/></p>
			<p> e ho <xsl:value-of select="zoo:age"/> anni.</p>
		</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>

