<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
	<html>
		<body>
		<h3>Descizione degli animali:</h3>
			<xsl:for-each select="zoo:animal">
				<p>--- Ciao, sono <xsl:value-of select="zoo:name"/>, </p>
				<p>sono un <xsl:value-of select="zoo:gender"/>,</p>
				<p>ho <xsl:value-of select="zoo:age"/> anni, </p>
				<p>vivo nella <xsl:value-of select="zoo:area/zoo:zona"/></p>
				<p>e sono: <xsl:value-of select="zoo:area/zoo:species"/>.</p>
			</xsl:for-each>
		</body>
	</html>
	</xsl:template>
</xsl:stylesheet>

